/**
 * Copyright 2021 Huawei Technologies Co., Ltd
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef MINDSPORE_CCSRC_FL_SERVER_COLLECTIVE_OPS_IMPL_H_
#define MINDSPORE_CCSRC_FL_SERVER_COLLECTIVE_OPS_IMPL_H_

#include <map>
#include <memory>
#include <string>
#include <vector>
#include <functional>
#include "common/fl_context.h"
#include "server/server_node.h"
#include "common/common.h"

namespace mindspore {
namespace fl {
namespace server {
// The timeout for server collective communication in case of network jitter.
constexpr uint32_t kCollectiveCommTimeout = 30;
// The max timeout for server collective communication, used in disaster recovery to prevent networking flapping.
constexpr uint32_t kCollectiveCommMaxTimeout = 300;

// CollectiveOpsImpl is the collective communication API of the server.
// For now, it implements two AllReduce algorithms: RingAllReduce and BroadcastAllReduce. Elastic AllReduce is also
// supported for the elastic scaling feature of the server.
class CollectiveOpsImpl {
 public:
  static CollectiveOpsImpl &GetInstance() {
    static CollectiveOpsImpl instance;
    return instance;
  }

  void Initialize(const std::shared_ptr<ServerNode> &server_node);

  template <typename T>
  bool AllReduce(const std::string &data_name, void *sendbuff, void *recvbuff, size_t count,
                 const std::map<std::string, std::string> &server_map);

 private:
  CollectiveOpsImpl() : server_node_(nullptr), node_(nullptr), node_role_(NodeRole::WORKER), rank_size_(0) {}
  ~CollectiveOpsImpl() = default;
  CollectiveOpsImpl(const CollectiveOpsImpl &) = delete;
  CollectiveOpsImpl &operator=(const CollectiveOpsImpl &) = delete;

  // Implementation of RingAllReduce.
  template <typename T>
  bool RunRingAllReduce(const std::string &data_name, uint32_t send_to_rank, uint32_t recv_from_rank,
                        const std::vector<size_t> &chunk_sizes, const std::vector<size_t> &chunk_offset,
                        T *output_buff);

  // Implementation of RingAllReduce.
  template <typename T>
  bool RingAllReduce(const std::string &data_name, const void *sendbuff, void *recvbuff, size_t count);

  // Implementation of BroadcastAllReduce.
  template <typename T>
  bool ReduceBroadcastAllReduce(const std::string &data_name, const void *sendbuff, void *recvbuff, size_t count);

  std::shared_ptr<ServerNode> server_node_;
  std::string node_id_;

  // The mutex to ensure that collective communication is threadsafe.
  std::mutex mtx_;

  // The abstract node could be worker or server. Only nodes which have the same role could use collective
  // communication.
  std::shared_ptr<ServerNode> node_;
  NodeRole node_role_;
  size_t rank_size_ = 0;
  size_t rank_id_ = 0;
  std::vector<std::pair<std::string, std::string>> server_nodes_;
};
}  // namespace server
}  // namespace fl
}  // namespace mindspore
#endif  // MINDSPORE_CCSRC_FL_SERVER_COLLECTIVE_OPS_IMPL_H_
