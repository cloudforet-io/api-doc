---
title: "JobTask"
linkTitle: "JobTask"
weight: 3
bookFlatSection: true
---
# [JobTask](#JobTask)
A JobTask is a task unit subdividing a Job. The division criteria are specified in each DataSource plugin.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## JobTask





**JobTask Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**get**](./JobTask#get) | [JobTaskRequest](JobTask#jobtaskrequest) | [JobTaskInfo](JobTask#jobtaskinfo) |
| [**list**](./JobTask#list) | [JobTaskQuery](JobTask#jobtaskquery) | [JobTasksInfo](JobTask#jobtasksinfo) |
| [**stat**](./JobTask#stat) | [JobTaskStatQuery](JobTask#jobtaskstatquery) | [Struct](JobTask#struct) |



    
<br>

### get

Gets a specific JobTask. Prints detailed information about the JobTask, including the relevant resources: DataSource and Job. The criteria used for dividing a Job into JobTasks can be found in the DataSource used, but the total count of divided JobTasks can be found by this method.



> **POST** /cost-analysis/v1/job-task/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[JobTaskRequest](./JobTask#jobtaskrequest)

* **job_task_id** (string)   `Required` 





{{< highlight json >}}
{
   "job_task_id": "job-task-3622d860a776"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[JobTaskInfo](#JOBTASKINFO)
* **job_task_id** (string)   `Required` 

* **status** (Status)   `Required` 

* **options** (Struct)   `Required` 

* **changed** (ChangedInfo)   `Required` 

* **created_count** (int32)   `Required` 

* **error_code** (string)   `Required` 

* **error_message** (string)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **job_id** (string)   `Required` 

* **data_source_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **started_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **finished_at** (string)   `Required` 



{{< highlight json >}}
{
   "job_task_id": "job-task-3622d860a776",
   "status": "SUCCESS",
   "options": {
       "month": "202207",
       "platform": "gcp"
   },
   "changed": {
       "start": "2024-12",
       "end": "2025-01",
       "filter": {
           "additional_info.Account ID": "3241123123"
       }
   },
   "created_count": 1,
   "job_id": "job-85cf2c385252",
   "data_source_id": "ds-c96609f5afeb",
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-07-17T16:00:08.266Z",
   "started_at": "2022-07-17T16:01:28.243Z",
   "updated_at": "2022-07-17T16:01:28.939Z",
   "finished_at": "2022-07-17T16:01:28.939Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all JobTasks. You can use a query to get a filtered list of JobTasks.



> **POST** /cost-analysis/v1/job-task/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[JobTaskQuery](./JobTask#jobtaskquery)

* **query** (Query)  


* **job_task_id** (string)  


* **status** (Status)  


* **workspace_id** (string)  


* **job_id** (string)  


* **data_source_id** (string)  





{{< highlight json >}}
{
   "data_source_id": "ds-12asdsf2a",
   "query": {}
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
           "job_task_id": "job-task-3622d860a776",
           "status": "SUCCESS",
           "options": {
               "platform": "gcp",
               "month": "202207"
           },
           "created_count": 1,
           "job_id": "job-85cf2c385252",
           "data_source_id": "ds-c96609f5afeb",
           "domain_id": "domain-58010aa2e451",
           "created_at": "2022-07-17T16:00:08.266Z",
           "started_at": "2022-07-17T16:01:28.243Z",
           "updated_at": "2022-07-17T16:01:28.939Z",
           "finished_at": "2022-07-17T16:01:28.939Z"
       },
       {
           "job_task_id": "job-task-038c0b076ec5",
           "status": "SUCCESS",
           "options": {
               "account": "257706363616",
               "start": "2022-07-01"
           },
           "created_count": 5756,
           "job_id": "job-6b6765f757a9",
           "data_source_id": "ds-fcba92ca73b1",
           "domain_id": "domain-58010aa2e451",
           "created_at": "2022-07-17T16:00:05.099Z",
           "started_at": "2022-07-17T16:00:47.356Z",
           "updated_at": "2022-07-17T16:01:20.856Z",
           "finished_at": "2022-07-17T16:01:20.856Z"
       }
   ],
   "total_count": 720
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /cost-analysis/v1/job-task/stat
>






    


<br>
<br>

## Message



### JobTaskInfo
* **job_task_id** (string)   `Required` 

    
* **status** (Status)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **changed** (ChangedInfo)   `Required` 

    
* **created_count** (int32)   `Required` 

    
* **error_code** (string)   `Required` 

    
* **error_message** (string)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **job_id** (string)   `Required` 

    
* **data_source_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **started_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    
* **finished_at** (string)   `Required` 

    <br>

### JobTaskQuery
* **query** (Query)  

    
* **job_task_id** (string)  

    
* **status** (Status)  

    
* **workspace_id** (string)  

    
* **job_id** (string)  

    
* **data_source_id** (string)  

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
