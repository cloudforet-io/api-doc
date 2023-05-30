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
| [**get**](./Note#get) | [GetNoteRequest](Note#getnoterequest) | [NoteInfo](Note#noteinfo) |
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

  *is_required: true*


* **note** (string)   `Required` 

  *is_required: true*


* **domain_id** (string)   `Required` 

  *is_required: true*





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

  *is_required: true*


* **note** (string)   `Required` 

  *is_required: false*


* **domain_id** (string)   `Required` 

  *is_required: true*





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

  *is_required: true*


* **domain_id** (string)   `Required` 

  *is_required: true*





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



[GetNoteRequest](./Note#getnoterequest)

* **note_id** (string)   `Required` 

  *is_required: true*


* **domain_id** (string)   `Required` 

  *is_required: true*


* **only** (string)  `Repeated`    `Required` 

  *is_required: false*





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

* **query** (Query)   `Required` 

  *is_required: false*


* **note_id** (string)   `Required` 

  *is_required: false*


* **record_id** (string)   `Required` 

  *is_required: false*


* **cloud_service_id** (string)   `Required` 

  *is_required: false*


* **created_by** (string)   `Required` 

  *is_required: false*


* **domain_id** (string)   `Required` 

  *is_required: false*





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

  *is_required: true*

    
* **note** (string)   `Required` 

  *is_required: true*

    
* **domain_id** (string)   `Required` 

  *is_required: true*

    <br>

### GetNoteRequest
* **note_id** (string)   `Required` 

  *is_required: true*

    
* **domain_id** (string)   `Required` 

  *is_required: true*

    
* **only** (string)  `Repeated`    `Required` 

  *is_required: false*

    <br>

### NoteInfo
* **note_id** (string)   `Required` 

    
* **record_id** (string)   `Required` 

    
* **cloud_service_id** (string)   `Required` 

    
* **note** (string)   `Required` 

    
* **created_by** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### NoteQuery
* **query** (Query)   `Required` 

  *is_required: false*

    
* **note_id** (string)   `Required` 

  *is_required: false*

    
* **record_id** (string)   `Required` 

  *is_required: false*

    
* **cloud_service_id** (string)   `Required` 

  *is_required: false*

    
* **created_by** (string)   `Required` 

  *is_required: false*

    
* **domain_id** (string)   `Required` 

  *is_required: false*

    <br>

### NoteRequest
* **note_id** (string)   `Required` 

  *is_required: true*

    
* **domain_id** (string)   `Required` 

  *is_required: true*

    <br>

### NoteStatQuery
* **query** (StatisticsQuery)   `Required` 

  *is_required: true*

    
* **domain_id** (string)   `Required` 

  *is_required: true*

    <br>

### NotesInfo
* **results** (NoteInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateNoteRequest
* **note_id** (string)   `Required` 

  *is_required: true*

    
* **note** (string)   `Required` 

  *is_required: false*

    
* **domain_id** (string)   `Required` 

  *is_required: true*

    <br>
