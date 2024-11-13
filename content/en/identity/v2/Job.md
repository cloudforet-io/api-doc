---
title: "Job"
linkTitle: "Job"
weight: 3
bookFlatSection: true
---
# [Job](#Job)
A Job is an act of collecting external cloud resources through plugins.


>  **Package : spaceone.api.identity.v2**

<br>
<br>

## Job





**Job Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**delete**](./Job#delete) | [JobRequest](Job#jobrequest) | [Empty](Job#empty) |
| [**get**](./Job#get) | [JobRequest](Job#jobrequest) | [JobInfo](Job#jobinfo) |
| [**list**](./Job#list) | [JobsQuery](Job#jobsquery) | [JobsInfo](Job#jobsinfo) |
| [**stat**](./Job#stat) | [JobStatQuery](Job#jobstatquery) | [Struct](Job#struct) |



    
<br>

### delete

Deletes a specific Job. You must specify the `job_id` of the Job to delete.



> **POST** /identity/v2/job/delete
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

Gets a specific Job. Prints detailed information about the Job, including its state.



> **POST** /identity/v2/job/get
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

* **options** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **error_message** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **plugin_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **finished_at** (string)   `Required` 



{{< highlight json >}}
{
     "job_id": "job-123456789012",
     "status": "ERROR",
     "resource_group": "DOMAIN",
     "plugin_id": "plugin-aws-cloud-service-inven-collector",
     "trusted_account_id": "ta-123456789012",
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



> **POST** /identity/v2/job/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[JobsQuery](./Job#jobsquery)

* **query** (Query)  


* **job_id** (string)  


* **status** (JobStatus)  


* **workspace_id** (string)  


* **trusted_account_id** (string)  


* **plugin_id** (string)  





{{< highlight json >}}
{
   "query": {
       "page": {
           "start": 1,
           "limit": 10
       }
   },
   "trusted_account_id": "ta-123456789012"
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
           "resource_group": "DOMAIN",
           "plugin_id": "plugin-aws-cloud-service-inven-collector",
           "trusted_account_id": "ta-3b124006c2d2",
           "domain_id": "domain-58010aa2e451",
           "created_at": "2022-06-17T08:00:01.225Z",
           "updated_at": "2022-06-17T08:00:01.225Z",
           "finished_at": "2022-06-17T08:00:15.197Z"
       },
       {
           "job_id": "job-587a3d3b4db3",
           "status": "SUCCESS",
           "resource_group": "DOMAIN",
           "plugin_id": "plugin-aws-cloud-service-inven-collector",
           "trusted_account_id": "ta-587a3d3b4db3",
           "domain_id": "domain-58010aa2e451",
           "created_at": "2022-06-17T08:00:00.407Z",
           "updated_at": "2022-06-17T08:00:00.407Z",
           "finished_at": "2022-06-17T08:07:32.023Z"
       }
   ],
   "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /identity/v2/job/stat
>






    


<br>
<br>

## Message



### JobInfo
* **job_id** (string)   `Required` 

    
* **status** (Status)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **error_message** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **trusted_account_id** (string)   `Required` 

    
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

    
* **trusted_account_id** (string)  

    
* **plugin_id** (string)  

    <br>
