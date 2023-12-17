---
title: "Note"
linkTitle: "Note"
weight: 3
bookFlatSection: true
---
# [Note](#Note)



>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## Note





**Note Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Note#create) | [CreateNoteRequest](Note#createnoterequest) | [NoteInfo](Note#noteinfo) |
| [**update**](./Note#update) | [UpdateNoteRequest](Note#updatenoterequest) | [NoteInfo](Note#noteinfo) |
| [**delete**](./Note#delete) | [NoteRequest](Note#noterequest) | [Empty](Note#empty) |
| [**get**](./Note#get) | [NoteRequest](Note#noterequest) | [NoteInfo](Note#noteinfo) |
| [**list**](./Note#list) | [NoteQuery](Note#notequery) | [NotesInfo](Note#notesinfo) |
| [**stat**](./Note#stat) | [NoteStatQuery](Note#notestatquery) | [Struct](Note#struct) |



    
<br>

### create





> **POST** /inventory/v1/note/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateNoteRequest](./Note#createnoterequest)

* **record_id** (string)   `Required` 


* **note** (string)   `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NoteInfo](#NOTEINFO)
* **note_id** (string)   `Required` 

* **record_id** (string)   `Required` 

* **cloud_service_id** (string)   `Required` 

* **note** (string)   `Required` 

* **created_by** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update





> **POST** /inventory/v1/note/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateNoteRequest](./Note#updatenoterequest)

* **note_id** (string)   `Required` 


* **note** (string)  





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NoteInfo](#NOTEINFO)
* **note_id** (string)   `Required` 

* **record_id** (string)   `Required` 

* **cloud_service_id** (string)   `Required` 

* **note** (string)   `Required` 

* **created_by** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete





> **POST** /inventory/v1/note/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[NoteRequest](./Note#noterequest)

* **note_id** (string)   `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get





> **POST** /inventory/v1/note/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[NoteRequest](./Note#noterequest)

* **note_id** (string)   `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NoteInfo](#NOTEINFO)
* **note_id** (string)   `Required` 

* **record_id** (string)   `Required` 

* **cloud_service_id** (string)   `Required` 

* **note** (string)   `Required` 

* **created_by** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list





> **POST** /inventory/v1/note/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[NoteQuery](./Note#notequery)

* **query** (Query)  


* **note_id** (string)  


* **record_id** (string)  


* **cloud_service_id** (string)  


* **created_by** (string)  


* **workspace_id** (string)  


* **project_id** (string)  





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### stat





> **POST** /inventory/v1/note/stat
>






    


<br>
<br>

## Message



### CreateNoteRequest
* **record_id** (string)   `Required` 

    
* **note** (string)   `Required` 

    <br>

### NoteInfo
* **note_id** (string)   `Required` 

    
* **record_id** (string)   `Required` 

    
* **cloud_service_id** (string)   `Required` 

    
* **note** (string)   `Required` 

    
* **created_by** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### NoteQuery
* **query** (Query)  

    
* **note_id** (string)  

    
* **record_id** (string)  

    
* **cloud_service_id** (string)  

    
* **created_by** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### NoteRequest
* **note_id** (string)   `Required` 

    <br>

### NoteStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### NotesInfo
* **results** (NoteInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateNoteRequest
* **note_id** (string)   `Required` 

    
* **note** (string)  

    <br>
