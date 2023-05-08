---
title: "Job_task"
linkTitle: "Job_task"
weight: 3
bookFlatSection: true
---
# [Job_task](#Job_task)
desc: A JobTask is a unit for collecting external cloud resources. The resource belongs to a specific service account.


>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## Job_task


**JobTask Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**delete**](./JobTask#delete) | [JobTaskRequest](JobTask#jobtaskrequest) | [Empty](./JobTask#empty) |
| [**get**](./JobTask#get) | [GetJobTaskRequest](JobTask#getjobtaskrequest) | [JobTaskInfo](./JobTask#jobtaskinfo) |
| [**list**](./JobTask#list) | [JobTaskQuery](JobTask#jobtaskquery) | [JobTasksInfo](./JobTask#jobtasksinfo) |
| [**stat**](./JobTask#stat) | [JobTaskStatQuery](JobTask#jobtaskstatquery) | [Struct](./JobTask#struct) |



    
<br>

### delete

> **POST** /inventory/v1/job-task/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /inventory/v1/job-task/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /inventory/v1/job-task/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /inventory/v1/job-task/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### GetJobTaskRequest
* **job_task_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### JobTaskInfo
* **job_task_id** (string)  `Required` 

    
* **status** (JobTaskStatus)  `Required` 

    
* **created_count** (int32)  `Required` 

    
* **updated_count** (int32)  `Required` 

    
* **failure_count** (int32)  `Required` 

    
* **deleted_count** (int32)  `Required` 

    
* **disconnected_count** (int32)  `Required` 

    
* **errors** (ErrorInfo)  `Required` 

    
* **job_id** (string)  `Required` 

    
* **secret_id** (string)  `Required` 

    
* **provider** (string)  `Required` 

    
* **service_account_id** (string)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **started_at** (string)  `Required` 

    
* **finished_at** (string)  `Required` 

    <br>

### JobTaskQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **job_task_id** (string)  `Required` 

  *is_required: false*

    
* **status** (JobTaskStatus)  `Required` 

  *is_required: false*

    
* **job_id** (string)  `Required` 

  *is_required: false*

    
* **secret_id** (string)  `Required` 

  *is_required: false*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **service_account_id** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### JobTaskRequest
* **job_task_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### JobTaskStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### JobTasksInfo
* **results** (JobTaskInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>
