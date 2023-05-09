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

desc: Creates a new Note. You can create Notes for each Alert to record the information needed to manage the Alerts.
request_example: >-
{
"alert_id": "alert-160ce04f6908",
"note": "This is a description",
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"note_id": "note-df107d31bf20",
"alert_id": "alert-160ce04f6908",
"note": "This is a description",
"created_by": "seolmin@mz.co.kr",
"project_id": "project-52a423012d5e",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-29T08:26:14.418Z"
}



> **POST** /monitoring/v1/note/create
>






    
<br>

### update

desc: Updates a specific Note. You must specify the `note_id` for Note validation check. If the Note exists, it is updated.
request_example: >-
{
"note_id": "note-df107d31bf20",
"note": "This is a test",
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"note_id": "note-df107d31bf20",
"alert_id": "alert-160ce04f6908",
"note": "This is a test",
"created_by": "seolmin@mz.co.kr",
"project_id": "project-52a423012d5e",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-29T08:26:14.418Z"
}



> **POST** /monitoring/v1/note/update
>






    
<br>

### delete

desc: Deletes a specific Note. You must specify the `note_id` of the Note to delete.
request_example: >-
{
"note_id": "note-0bfac585bf5a",
"domain_id": "domain-58010aa2e451"
}



> **POST** /monitoring/v1/note/delete
>






    
<br>

### get

desc: Gets a specific Note. You must specify the `note_id` and `domain_id`.
request_example: >-
{
"note_id": "note-0bfac585bf5a",
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"note_id": "note-0bfac585bf5a",
"alert_id": "alert-fbfd78e43df8",
"note": "test",
"created_by": "hykang@mz.co.kr",
"project_id": "project-52a423012d5e",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-23T09:52:42.251Z"
}



> **POST** /monitoring/v1/note/get
>






    
<br>

### list

desc: Gets a list of all Notes. You can use a query to get a filtered list of Notes.
request_example: >-
{
"query": {},
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"results": [
{
"note_id": "note-0597bd748be0",
"alert_id": "alert-fbfd78e43df8",
"note": "http://spaceone.org",
"created_by": "hykang@mz.co.kr",
"project_id": "project-52a423012d5e",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-23T09:58:23.838Z"
},
{
"note_id": "note-0bfac585bf5a",
"alert_id": "alert-fbfd78e43df8",
"note": "test",
"created_by": "hykang@mz.co.kr",
"project_id": "project-52a423012d5e",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-23T09:52:42.251Z"
}
],
"total_count": 2
}



> **POST** /monitoring/v1/note/list
>






    
<br>

### stat





> **POST** /monitoring/v1/note/stat
>






    


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
