---
title: "JobTask"
linkTitle: "JobTask"
weight: 3
bookFlatSection: true
---
# [JobTask](#JobTask)
A JobTask is a unit for collecting external cloud resources. The resource belongs to a specific service account.


>  **Package : spaceone.api.inventory_v2.v1**

<br>
<br>

## JobTask





**JobTask Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**delete**](./JobTask#delete) | [JobTaskRequest](JobTask#jobtaskrequest) | [Empty](JobTask#empty) |
| [**get**](./JobTask#get) | [JobTaskRequest](JobTask#jobtaskrequest) | [JobTaskInfo](JobTask#jobtaskinfo) |
| [**get_detail**](./JobTask#get_detail) | [JobTaskRequest](JobTask#jobtaskrequest) | [JobTaskDetailInfo](JobTask#jobtaskdetailinfo) |
| [**list**](./JobTask#list) | [JobTaskQuery](JobTask#jobtaskquery) | [JobTasksInfo](JobTask#jobtasksinfo) |
| [**stat**](./JobTask#stat) | [JobTaskStatQuery](JobTask#jobtaskstatquery) | [Struct](JobTask#struct) |



    
<br>

### delete

Deletes a specific JobTask. You must specify the `job_task_id` of the JobTask to delete.



> **POST** /inventory-v2/v1/job-task/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[JobTaskRequest](./JobTask#jobtaskrequest)

* **job_task_id** (string)   `Required` 





{{< highlight json >}}
{
   "job_task_id": "job-task-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific JobTask. Prints detailed information about the JobTask, including its state, updated or failure counts, and error log.



> **POST** /inventory-v2/v1/job-task/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[JobTaskRequest](./JobTask#jobtaskrequest)

* **job_task_id** (string)   `Required` 





{{< highlight json >}}
{
   "job_task_id": "job-task-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[JobTaskInfo](#JOBTASKINFO)
* **job_task_id** (string)   `Required` 

* **status** (JobTaskStatus)   `Required` 

* **provider** (string)   `Required` 

* **created_count** (int32)   `Required` 

* **updated_count** (int32)   `Required` 

* **failure_count** (int32)   `Required` 

* **deleted_count** (int32)   `Required` 

* **disconnected_count** (int32)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **collector_id** (string)   `Required` 

* **service_account_id** (string)   `Required` 

* **job_id** (string)   `Required` 

* **secret_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **started_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **finished_at** (string)   `Required` 



{{< highlight json >}}
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
     "collector_id": "collector-123456789012",
     "project_id": "project-123456789012",
     "domain_id": "domain-123456789012",
     "created_at": "2022-01-01T11:00:02.588Z",
     "started_at": "2022-01-01T11:00:02.819Z",
     "finished_at": "2022-01-01T11:00:34.398Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get_detail





> **POST** /inventory-v2/v1/job-task/get-detail
>





 {{< tabs " get_detail " >}}

 {{< tab "Request Example" >}}



[JobTaskRequest](./JobTask#jobtaskrequest)

* **job_task_id** (string)   `Required` 





{{< highlight json >}}
{
   "job_task_id": "job-task-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### list

Gets a list of all JobTasks in a specific Job. You can use a query to get a filtered list of JobTasks.



> **POST** /inventory-v2/v1/job-task/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[JobTaskQuery](./JobTask#jobtaskquery)

* **query** (Query)  


* **job_task_id** (string)  


* **status** (JobTaskStatus)  


* **provider** (string)  


* **workspace_id** (string)  


* **project_id** (string)  


* **service_account_id** (string)  


* **job_id** (string)  


* **secret_id** (string)  





{{< highlight json >}}
{
   "query": {
       "filter": [
           {
               "key": "status",
               "value": "FAILURE",
               "operator": "eq"
           }
       ],
       "page": {
           "start": 1,
           "limit": 5
       }
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[JobTasksInfo](#JOBTASKSINFO)
* **results** (JobTaskInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
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
           "project_id": "project-77dfad3f7cd3",
           "domain_id": "domain-58010aa2e451",
           "workspace_id": "workspace-78099aa2e451",
           "created_at": "2022-06-17T08:00:00.680Z",
           "started_at": "2022-06-17T08:00:00.914Z",
           "updated_at": "2022-06-17T08:00:00.814Z",
           "finished_at": "2022-06-17T08:05:48.933Z"
       },
       {
           "job_task_id": "job_task-c5077338cf23",
           "status": "SUCCESS",
           "created_count": 123,
           "updated_count": 1921,
           "job_id": "job-587a3d3b4db3",
           "secret_id": "secret-1cd7417c1889",
           "provider": "aws",
           "service_account_id": "sa-5e186fcc7c91",
           "project_id": "project-18655561c535",
           "workspace_id": "workspace-1c1b7b7b7b7b",
           "domain_id": "domain-58010aa2e451",
           "created_at": "2022-06-17T08:00:00.582Z",
           "started_at": "2022-06-17T08:00:00.814Z",
           "updated_at": "2022-06-17T08:00:00.814Z",
           "finished_at": "2022-06-17T08:07:31.995Z"
       }
   ],
   "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /inventory-v2/v1/job-task/stat
>






    


<br>
<br>

## Message



### ErrorInfo
* **error_code** (string)   `Required` 

    
* **message** (string)   `Required` 

    
* **additional** (Struct)   `Required` 

    <br>

### JobTaskDetailInfo
* **job_task_id** (string)   `Required` 

    
* **created_info** (Struct)   `Required` 

    
* **updated_info** (Struct)   `Required` 

    
* **failure_info** (Struct)   `Required` 

    
* **deleted_info** (Struct)   `Required` 

    
* **disconnected_info** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **job_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### JobTaskInfo
* **job_task_id** (string)   `Required` 

    
* **status** (JobTaskStatus)   `Required` 

    
* **provider** (string)   `Required` 

    
* **created_count** (int32)   `Required` 

    
* **updated_count** (int32)   `Required` 

    
* **failure_count** (int32)   `Required` 

    
* **deleted_count** (int32)   `Required` 

    
* **disconnected_count** (int32)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **collector_id** (string)   `Required` 

    
* **service_account_id** (string)   `Required` 

    
* **job_id** (string)   `Required` 

    
* **secret_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **started_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    
* **finished_at** (string)   `Required` 

    <br>

### JobTaskQuery
* **query** (Query)  

    
* **job_task_id** (string)  

    
* **status** (JobTaskStatus)  

    
* **provider** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    
* **service_account_id** (string)  

    
* **job_id** (string)  

    
* **secret_id** (string)  

    <br>

### JobTaskRequest
* **job_task_id** (string)   `Required` 

    <br>

### JobTaskStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### JobTasksInfo
* **results** (JobTaskInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
