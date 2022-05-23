/**
 * Copyright 2021-2022 Huawei Technologies Co., Ltd
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

#ifndef MINDSPORE_CCSRC_BACKEND_KERNEL_COMPILER_FL_START_FL_JOB_H_
#define MINDSPORE_CCSRC_BACKEND_KERNEL_COMPILER_FL_START_FL_JOB_H_

#include <vector>
#include <string>
#include <memory>
#include "worker/kernel/abstract_kernel.h"
#include "worker/worker.h"
#include "common/fl_context.h"
#include "common/core/comm_util.h"
#include "common/utils/python_adapter.h"
#include "server/local_meta_store.h"

namespace mindspore {
namespace fl {
namespace worker {
namespace kernel {
class StartFLJobKernelMod : public AbstractKernel {
 public:
  StartFLJobKernelMod() = default;
  ~StartFLJobKernelMod() override = default;

  static std::shared_ptr<StartFLJobKernelMod> GetInstance() {
    static std::shared_ptr<StartFLJobKernelMod> instance = nullptr;
    if (instance == nullptr) {
      instance.reset(new StartFLJobKernelMod());
      instance->Init();
    }
    return instance;
  }

  bool Launch(size_t data_size) {
    MS_LOG(INFO) << "Launching client StartFLJobKernelMod";
    FBBuilder fbb;
    if (!BuildStartFLJobReq(&fbb, data_size)) {
      MS_LOG(EXCEPTION) << "Building request for StartFLJob failed.";
      return false;
    }

    std::shared_ptr<std::vector<unsigned char>> start_fl_job_rsp_msg = nullptr;
    if (!fl::worker::Worker::GetInstance().SendToServer(fbb.GetBufferPointer(), fbb.GetSize(),
                                                        fl::TcpUserCommand::kStartFLJob, &start_fl_job_rsp_msg)) {
      MS_LOG(EXCEPTION) << "Sending request for StartFLJob to server failed.";
      return false;
    }
    flatbuffers::Verifier verifier(start_fl_job_rsp_msg->data(), start_fl_job_rsp_msg->size());
    if (!verifier.VerifyBuffer<schema::ResponseFLJob>()) {
      MS_LOG(EXCEPTION) << "The schema of ResponseFLJob is invalid.";
      return false;
    }

    const schema::ResponseFLJob *start_fl_job_rsp =
      flatbuffers::GetRoot<schema::ResponseFLJob>(start_fl_job_rsp_msg->data());
    MS_EXCEPTION_IF_NULL(start_fl_job_rsp);
    auto response_code = start_fl_job_rsp->retcode();
    switch (response_code) {
      case schema::ResponseCode_SUCCEED:
      case schema::ResponseCode_OutOfTime:
        break;
      default:
        MS_LOG(EXCEPTION) << "Launching start fl job for worker failed. Reason: " << start_fl_job_rsp->reason();
    }
    fl::worker::Worker::GetInstance().set_data_size(data_size);
    uint64_t iteration = IntToSize(start_fl_job_rsp->iteration());
    fl::worker::Worker::GetInstance().set_fl_iteration_num(iteration);
    MS_LOG(INFO) << "Start fl job for iteration " << iteration;
    return true;
  }

  void Init() override {
    fl_name_ = fl::worker::Worker::GetInstance().fl_name();
    fl_id_ = fl::worker::Worker::GetInstance().fl_id();
    MS_LOG(INFO) << "Initializing StartFLJob kernel. fl_name: " << fl_name_ << ", fl_id: " << fl_id_;
  }

 private:
  bool BuildStartFLJobReq(FBBuilder *fbb, size_t data_size) {
    MS_EXCEPTION_IF_NULL(fbb);
    auto fbs_fl_name = fbb->CreateString(fl_name_);
    auto fbs_fl_id = fbb->CreateString(fl_id_);
    auto time = fl::CommUtil::GetNowTime();
    MS_LOG(INFO) << "now time: " << time.time_str_mill;
    auto fbs_timestamp = fbb->CreateString(std::to_string(time.time_stamp));
    schema::RequestFLJobBuilder req_fl_job_builder(*fbb);
    req_fl_job_builder.add_fl_name(fbs_fl_name);
    req_fl_job_builder.add_fl_id(fbs_fl_id);
    req_fl_job_builder.add_data_size(data_size);
    req_fl_job_builder.add_timestamp(fbs_timestamp);
    auto req_fl_job = req_fl_job_builder.Finish();
    fbb->Finish(req_fl_job);
    return true;
  }
  std::string fl_name_;
  std::string fl_id_;
};
}  // namespace kernel
}  // namespace worker
}  // namespace fl
}  // namespace mindspore

#endif  // MINDSPORE_CCSRC_BACKEND_KERNEL_COMPILER_FL_START_FL_JOB_H_
