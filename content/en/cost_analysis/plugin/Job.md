---
title: "Job"
linkTitle: "Job"
weight: 3
bookFlatSection: true
---
# [Job](#Job)



>  **Package : spaceone.api.cost_analysis.plugin**

<br>
<br>

## Job





**Job Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**get_tasks**](./Job#get_tasks) | [GetTasksRequest](Job#gettasksrequest) | [TasksInfo](Job#tasksinfo) |



    
<br>

### get_tasks









 {{< tabs " get_tasks " >}}

 {{< tab "Request Example" >}}



[GetTasksRequest](./Job#gettasksrequest)

* **options** (Struct)   `Required` 


* **secret_data** (Struct)   `Required` 


* **domain_id** (string)   `Required` 


* **linked_accounts** (Struct)  `Repeated`    `Required` 


* **schema** (string)  


* **start** (string)  


* **last_synchronized_at** (string)  





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[TasksInfo](#TASKSINFO)
* **tasks** (TaskInfo)  `Repeated`   `Required` 

* **changed** (ChangedInfo)  `Repeated`   `Required` 

* **synced_accounts** (SyncedAccountInfo)  `Repeated`   `Required` 



{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    


<br>
<br>

## Message



### ChangedInfo
* **start** (string)   `Required` 

    
* **end** (string)   `Required` 

    
* **filter** (Struct)   `Required` 

    <br>

### GetTasksRequest
* **options** (Struct)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **linked_accounts** (Struct)  `Repeated`    `Required` 

    
* **schema** (string)  

    
* **start** (string)  

    
* **last_synchronized_at** (string)  

    <br>

### SyncedAccountInfo
* **account_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    <br>

### TaskInfo
* **task_options** (Struct)   `Required` 

    
* **task_changed** (ChangedInfo)  

    <br>

### TasksInfo
* **tasks** (TaskInfo)  `Repeated`    `Required` 

    
* **changed** (ChangedInfo)  `Repeated`    `Required` 

    
* **synced_accounts** (SyncedAccountInfo)  `Repeated`    `Required` 

    <br>
