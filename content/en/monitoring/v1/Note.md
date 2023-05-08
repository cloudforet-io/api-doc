---
title: "Note"
linkTitle: "Note"
weight: 3
bookFlatSection: true
---
# [Note](#Note)
desc: A Note is a comment on an Event, and is used for incident management.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## Note


**Note Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Note#create) | [CreateNoteRequest](Note#createnoterequest) | [NoteInfo](./Note#noteinfo) |
| [**update**](./Note#update) | [UpdateNoteRequest](Note#updatenoterequest) | [NoteInfo](./Note#noteinfo) |
| [**delete**](./Note#delete) | [NoteRequest](Note#noterequest) | [Empty](./Note#empty) |
| [**get**](./Note#get) | [GetNoteRequest](Note#getnoterequest) | [NoteInfo](./Note#noteinfo) |
| [**list**](./Note#list) | [NoteQuery](Note#notequery) | [NotesInfo](./Note#notesinfo) |
| [**stat**](./Note#stat) | [NoteStatQuery](Note#notestatquery) | [Struct](./Note#struct) |



    
<br>

### create

> **POST** /monitoring/v1/note/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /monitoring/v1/note/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /monitoring/v1/note/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /monitoring/v1/note/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /monitoring/v1/note/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /monitoring/v1/note/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateNoteRequest
* **alert_id** (string)  `Required` 

  *is_required: true*

    
* **note** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetNoteRequest
* **note_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### NoteInfo
* **note_id** (string)  `Required` 

    
* **alert_id** (string)  `Required` 

    
* **note** (string)  `Required` 

    
* **created_by** (string)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### NoteQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **note_id** (string)  `Required` 

  *is_required: false*

    
* **alert_id** (string)  `Required` 

  *is_required: false*

    
* **created_by** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>

### NoteRequest
* **note_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### NoteStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### NotesInfo
* **results** (NoteInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateNoteRequest
* **note_id** (string)  `Required` 

  *is_required: true*

    
* **note** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
