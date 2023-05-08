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
| [**get_tasks**](./Job#get_tasks) | [GetTasksRequest](Job#gettasksrequest) | [TasksInfo](./Job#tasksinfo) |



    
<br>

### get_tasks




 {{< tabs " get_tasks " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### ChangedInfo
* **start** (string)  `Required` 

    
* **end** (string)  `Required` 

    
* **filter** (Struct)  `Required` 

    <br>

### GetTasksRequest
* **options** (Struct)  `Required` 

  *is_required: true*

    
* **secret_data** (Struct)  `Required` 

  *is_required: true*

    
* **schema** (string)  `Required` 

  *is_required: false*

    
* **start** (string)  `Required` 

  *is_required: false*

    
* **last_synchronized_at** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### TaskInfo
* **task_options** (Struct)  `Required` 

    <br>

### TasksInfo
* **tasks** (TaskInfo)  `Required` 

    
* **changed** (ChangedInfo)  `Required` 

    <br>
