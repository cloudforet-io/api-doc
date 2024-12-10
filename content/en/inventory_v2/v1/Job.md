---
title: "Job"
linkTitle: "Job"
weight: 3
bookFlatSection: true
---
# [Job](#Job)
A Job is an act of collecting external cloud resources through plugins.


>  **Package : spaceone.api.inventory_v2.v1**

<br>
<br>

## Job





**Job Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**delete**](./Job#delete) | [JobRequest](Job#jobrequest) | [Empty](Job#empty) |
| [**get**](./Job#get) | [JobRequest](Job#jobrequest) | [JobInfo](Job#jobinfo) |
| [**list**](./Job#list) | [JobsQuery](Job#jobsquery) | [JobsInfo](Job#jobsinfo) |
| [**analyze**](./Job#analyze) | [JobAnalyzeQuery](Job#jobanalyzequery) | [Struct](Job#struct) |
| [**stat**](./Job#stat) | [JobStatQuery](Job#jobstatquery) | [Struct](Job#struct) |



    
<br>

### delete

Deletes a specific Job. You must specify the `job_id` of the Job to delete.



> **POST** /inventory-v2/v1/job/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[JobRequest](./Job#jobrequest)

* **job_id** (string)   `Required` 





{{< highlight json >}}
{
   "job_id": "job-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Job. Prints detailed information about the Job, including its state, total tasks, and collector info.



> **POST** /inventory-v2/v1/job/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[JobRequest](./Job#jobrequest)

* **job_id** (string)   `Required` 





{{< highlight json >}}
{
   "job_id": "job-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[JobInfo](#JOBINFO)
* **job_id** (string)   `Required` 

* **status** (Status)   `Required` 

* **total_tasks** (int32)   `Required` 

* **remained_tasks** (int32)   `Required` 

* **success_tasks** (int32)   `Required` 

* **failure_tasks** (int32)   `Required` 

* **request_secret_id** (string)   `Required` 

* **request_workspace_id** (string)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **collector_id** (string)   `Required` 

* **plugin_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **finished_at** (string)   `Required` 



{{< highlight json >}}
{
     "job_id": "job-123456789012",
     "status": "SUCCESS",
     "total_tasks": 2,
     "success_tasks": 2,
     "request_secret_id: "secret-123456789012",
     "request_workspace_id": "workspace-123456789012",
     "resource_group": "WORKSPACE"
     "workspace_id": "workspace-123456789012",
     "domain_id": "domain-123456789012",
     "created_at": "2022-01-01T10:00:01.389Z",
     "updated_at": "2022-01-01T10:00:01.389Z",
     "finished_at": "2022-01-01T10:02:11.270Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Jobs. You can use a query to get a filtered list of Jobs.



> **POST** /inventory-v2/v1/job/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[JobsQuery](./Job#jobsquery)

* **query** (Query)  


* **job_id** (string)  


* **status** (JobStatus)  


* **workspace_id** (string)  


* **collector_id** (string)  


* **plugin_id** (string)  





{{< highlight json >}}
{
   "query": {
       "page": {
           "start": 1,
           "limit": 5
       }
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[JobsInfo](#JOBSINFO)
* **results** (JobInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
   "results": [
       {
           "job_id": "job-3b124006c2d2",
           "status": "SUCCESS",
           "total_tasks": 2,
           "success_tasks": 2,
           "resource_group": "DOMAIN",
           "domain_id": "domain-58010aa2e451",
           "created_at": "2022-06-17T08:00:01.225Z",
           "updated_at": "2022-06-17T08:00:01.225Z",
           "finished_at": "2022-06-17T08:00:15.197Z"
       },
       {
           "job_id": "job-587a3d3b4db3",
           "status": "IN_PROGRESS",
           "total_tasks": 3,
           "success_tasks": 1,
           "remained_tasks": 1.
           "resource_group": "DOMAIN",
           "domain_id": "domain-58010aa2e451",
           "created_at": "2022-06-17T08:00:00.407Z",
           "updated_at": "2022-06-17T08:00:00.407Z",
           "finished_at": "2022-06-17T08:07:32.023Z"
       },
       {
          "job_id": "job-587a3d3b4db3",
          "status": "FAILURE",
          "total_tasks": 3,
          "success_tasks": 1,
          "failure_tasks": 1,
          "resource_group": "DOMAIN",
          "domain_id": "domain-58010aa2e451",
          "created_at": "2022-06-17T08:00:00.407Z",
          "updated_at": "2022-06-17T08:05:00.407Z",
          "finished_at": "2022-06-17T08:10:00.407Z"
       }

   ],
   "total_count": 3
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### analyze





> **POST** /inventory-v2/v1/job/analyze
>





 {{< tabs " analyze " >}}

 {{< tab "Request Example" >}}



[JobAnalyzeQuery](./Job#jobanalyzequery)

* **query** (AnalyzeQuery)   `Required` 





{{< highlight json >}}
{
 "query": {
     "group_by": ["job_id", "status"],
     "page": {
       "start": 1, "limit": 5
     },
     "fields": {
       "total_tasks_sum": {
         "key": "total_tasks",
         "operator": "sum"
        },
        "remain_tasks_sum": {
           "key": "remain_tasks",
           "operator": "sum"
        },
        "failure_tasks_sum": {
           "key": "failure_tasks",
           "operator": "sum"
        }
     }
  }
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### stat





> **POST** /inventory-v2/v1/job/stat
>





 {{< tabs " stat " >}}

 {{< tab "Request Example" >}}



[JobStatQuery](./Job#jobstatquery)

* **query** (StatisticsQuery)   `Required` 





{{< highlight json >}}
{
 "query": {
     "distinct": "status"
 }
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    


<br>
<br>

## Message



### JobAnalyzeQuery
* **query** (AnalyzeQuery)   `Required` 

    <br>

### JobInfo
* **job_id** (string)   `Required` 

    
* **status** (Status)   `Required` 

    
* **total_tasks** (int32)   `Required` 

    
* **remained_tasks** (int32)   `Required` 

    
* **success_tasks** (int32)   `Required` 

    
* **failure_tasks** (int32)   `Required` 

    
* **request_secret_id** (string)   `Required` 

    
* **request_workspace_id** (string)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **collector_id** (string)   `Required` 

    
* **plugin_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    
* **finished_at** (string)   `Required` 

    <br>

### JobRequest
* **job_id** (string)   `Required` 

    <br>

### JobStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### JobsInfo
* **results** (JobInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### JobsQuery
* **query** (Query)  

    
* **job_id** (string)  

    
* **status** (JobStatus)  

    
* **workspace_id** (string)  

    
* **collector_id** (string)  

    
* **plugin_id** (string)  

    <br>
