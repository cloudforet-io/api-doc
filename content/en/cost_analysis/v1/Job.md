---
title: "Job"
linkTitle: "Job"
weight: 3
bookFlatSection: true
---
# [Job](#Job)
A Job is an act of collecting external cost data through plugins. The data to collect is defined in a plugin.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## Job





**Job Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**cancel**](./Job#cancel) | [JobRequest](Job#jobrequest) | [JobInfo](./Job#jobinfo) |
| [**get**](./Job#get) | [GetJobRequest](Job#getjobrequest) | [JobInfo](./Job#jobinfo) |
| [**list**](./Job#list) | [JobQuery](Job#jobquery) | [JobsInfo](./Job#jobsinfo) |
| [**stat**](./Job#stat) | [JobStatQuery](Job#jobstatquery) | [Struct](./Job#struct) |



    
<br>

### cancel

Cancels a specific Job. You can manually cease a Job in run with this method.



> **POST** /cost-analysis/v1/job/cancel
>





 {{< tabs " cancel " >}}

 {{< tab "Request Example" >}}



[JobRequest](./Job#jobrequest)

* **job_id** (string)  `Required` 


* **domain_id** (string)  `Required` 





{{< highlight json >}}
{
   "job_id": "job-07994c7c9021"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[JobInfo](#JOBINFO)
* **job_id** (string)  `Required` 

* **status** (Status)  `Required` 

* **options** (Struct)  `Required` 

* **error_code** (string)  `Required` 

* **error_message** (string)  `Required` 

* **total_tasks** (int32)  `Required` 

* **remained_tasks** (int32)  `Required` 

* **data_source_id** (string)  `Required` 

* **domain_id** (string)  `Required` 

* **created_at** (string)  `Required` 

* **updated_at** (string)  `Required` 

* **finished_at** (string)  `Required` 

* **changed** (ChangedInfo)  `Required` 



{{< highlight json >}}
{
   "job_id": "job-07994c7c9021",
   "status": "CANCELED",
   "options": {
       "no_preload_cache": false,
       "start": "2021-01-01T00:00:00Z"
   },
   "total_tasks": 2,
   "remained_tasks": 2,
   "data_source_id": "ds-fcba92ca73b1",
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-04-02T09:17:44.031Z",
   "updated_at": "2022-04-02T09:19:47.715Z",
   "finished_at": "2022-04-02T09:19:47.715Z",
   "changed": [
       {
           "start": "2021-01-01T00:00:00.000Z"
       }
   ]
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get

Gets a specific Job. Prints detailed information about the Job, including the plugin used, operation time, and `status`.



> **POST** /cost-analysis/v1/job/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetJobRequest](./Job#getjobrequest)

* **job_id** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **only** (string) 





{{< highlight json >}}
{
   "job_id": "job-85cf2c385252"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[JobInfo](#JOBINFO)
* **job_id** (string)  `Required` 

* **status** (Status)  `Required` 

* **options** (Struct)  `Required` 

* **error_code** (string)  `Required` 

* **error_message** (string)  `Required` 

* **total_tasks** (int32)  `Required` 

* **remained_tasks** (int32)  `Required` 

* **data_source_id** (string)  `Required` 

* **domain_id** (string)  `Required` 

* **created_at** (string)  `Required` 

* **updated_at** (string)  `Required` 

* **finished_at** (string)  `Required` 

* **changed** (ChangedInfo)  `Required` 



{{< highlight json >}}
{
   "job_id": "job-07994c7c9021",
   "status": "CANCELED",
   "options": {
       "no_preload_cache": false,
       "start": "2021-01-01T00:00:00Z"
   },
   "total_tasks": 2,
   "remained_tasks": 2,
   "data_source_id": "ds-fcba92ca73b1",
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-04-02T09:17:44.031Z",
   "updated_at": "2022-04-02T09:19:47.715Z",
   "finished_at": "2022-04-02T09:19:47.715Z",
   "changed": [
       {
           "start": "2021-01-01T00:00:00.000Z"
       }
   ]
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Jobs. You can use a query to get a filtered list of Jobs.



> **POST** /cost-analysis/v1/job/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[JobQuery](./Job#jobquery)

* **domain_id** (string)  `Required` 


* **query** (Query) 


* **job_id** (string) 


* **status** (Status) 


* **data_source_id** (string) 





{{< highlight json >}}
{
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[JobsInfo](#JOBSINFO)
* **results** (JobInfo)  `Required` 

* **total_count** (int32)  `Required` 



{{< highlight json >}}
{
       "results": [
           {
               "job_id": "job-85cf2c385252",
               "status": "SUCCESS",
               "options": {
                   "start": null,
                   "no_preload_cache": false
               },
               "total_tasks": 1,
               "data_source_id": "ds-c96609f5afeb",
               "domain_id": "domain-58010aa2e451",
               "created_at": "2022-07-17T16:00:08.254Z",
               "updated_at": "2022-07-17T16:01:30.637Z",
               "finished_at": "2022-07-17T16:01:30.637Z",
               "changed": [
                   {
                       "start": "2022-07-01T00:00:00.000Z"
                   }
               ]
           },
           {
               "job_id": "job-6b6765f757a9",
               "status": "SUCCESS",
               "options": {
                   "start": null,
                   "no_preload_cache": false
               },
               "total_tasks": 2,
               "data_source_id": "ds-fcba92ca73b1",
               "domain_id": "domain-58010aa2e451",
               "created_at": "2022-07-17T16:00:05.077Z",
               "updated_at": "2022-07-17T16:01:28.206Z",
               "finished_at": "2022-07-17T16:01:28.206Z",
               "changed": [
                   {
                       "start": "2022-07-01T00:00:00.000Z"
                   }
               ]
           }
       ],
       "total_count": 372
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /cost-analysis/v1/job/stat
>






    


<br>
<br>

## Message



### ChangedInfo
* **start** (string)  `Required` 

    
* **end** (string)  `Required` 

    
* **filter** (Struct)  `Required` 

    <br>

### GetJobRequest
* **job_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **only** (string) 

    <br>

### JobInfo
* **job_id** (string)  `Required` 

    
* **status** (Status)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **error_code** (string)  `Required` 

    
* **error_message** (string)  `Required` 

    
* **total_tasks** (int32)  `Required` 

    
* **remained_tasks** (int32)  `Required` 

    
* **data_source_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    
* **finished_at** (string)  `Required` 

    
* **changed** (ChangedInfo)  `Required` 

    <br>

### JobQuery
* **domain_id** (string)  `Required` 

    
* **query** (Query) 

    
* **job_id** (string) 

    
* **status** (Status) 

    
* **data_source_id** (string) 

    <br>

### JobRequest
* **job_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### JobStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### JobsInfo
* **results** (JobInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>
