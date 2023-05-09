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

desc: Deletes a specific JobTask. You must specify the `job_task_id` of the JobTask to delete.
request_example: >-
{
"job_task_id": "job-task-123456789012",
"domain_id": "domain-123456789012"
}



> **POST** /inventory/v1/job-task/delete
>






    
<br>

### get

desc: Gets a specific JobTask. Prints detailed information about the JobTask, including its state, updated or failure counts, and error log.
request_example: >-
{
"job_task_id": "job-task-123456789012",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"job_task_id": "job-task-123456789012",
"status": "FAILURE",
"updated_count": 199,
"failure_count": 1,
"errors": [
{
"error_code": "ERROR_PLUGIN",
"message": "{\"tags\": [\"Could not interpret the value as a list\"]}",
"additional": {
"domain_id": "domain-123456789012",
"resource_id": "eventarc-us-central1-function",
"resource_type": "inventory.CloudService",
"cloud_service_group": "Pub/Sub",
"cloud_service_type": "Subscription",
"provider": "google_cloud"
}
}
],
"job_id": "job-123456789012",
"secret_id": "secret-123456789012",
"provider": "google_cloud",
"service_account_id": "sa-123456789012",
"project_id": "project-123456789012",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T11:00:02.588Z",
"started_at": "2022-01-01T11:00:02.819Z",
"finished_at": "2022-01-01T11:00:34.398Z"
}



> **POST** /inventory/v1/job-task/get
>






    
<br>

### list

desc: Gets a list of all JobTasks in a specific Job. You can use a query to get a filtered list of JobTasks.
request_example: >-
{
"query": {}
}
response_example: >-
{
"results": [
{
"job_task_id": "job_task-69b301d0fbfc",
"status": "SUCCESS",
"updated_count": 55,
"job_id": "job-587a3d3b4db3",
"secret_id": "secret-957e407bfc15",
"provider": "aws",
"service_account_id": "sa-a41ff4765671",
"project_id": "project-77dffd3f7cd3",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-17T08:00:00.680Z",
"started_at": "2022-06-17T08:00:00.914Z",
"finished_at": "2022-06-17T08:05:48.933Z"
},
{
"job_task_id": "job_task-c5077338cf23",
"status": "SUCCESS",
"updated_count": 1921,
"job_id": "job-587a3d3b4db3",
"secret_id": "secret-1cd7417c1889",
"provider": "aws",
"service_account_id": "sa-5e186fcc7c91",
"project_id": "project-18655561c535",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-17T08:00:00.582Z",
"started_at": "2022-06-17T08:00:00.814Z",
"finished_at": "2022-06-17T08:07:31.995Z"
}
],
"total_count": 4839
}



> **POST** /inventory/v1/job-task/list
>






    
<br>

### stat





> **POST** /inventory/v1/job-task/stat
>






    


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
