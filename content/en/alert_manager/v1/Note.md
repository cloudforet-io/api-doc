---
title: "Note"
linkTitle: "Note"
weight: 3
bookFlatSection: true
---
# [Note](#Note)



>  **Package : spaceone.api.alert_manager.v1**

<br>
<br>

## Note





**Note Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Note#create) | [NoteCreateRequest](Note#notecreaterequest) | [NoteInfo](Note#noteinfo) |
| [**update**](./Note#update) | [NoteUpdateRequest](Note#noteupdaterequest) | [NoteInfo](Note#noteinfo) |
| [**delete**](./Note#delete) | [NoteRequest](Note#noterequest) | [Empty](Note#empty) |
| [**get**](./Note#get) | [NoteRequest](Note#noterequest) | [NoteInfo](Note#noteinfo) |
| [**list**](./Note#list) | [NoteSearchQuery](Note#notesearchquery) | [NotesInfo](Note#notesinfo) |
| [**stat**](./Note#stat) | [NoteStatQuery](Note#notestatquery) | [Struct](Note#struct) |



    
<br>

### create





> **POST** /alert-manager/v1/note/create
>






    
<br>

### update





> **POST** /alert-manager/v1/note/update
>






    
<br>

### delete





> **POST** /alert-manager/v1/note/delete
>






    
<br>

### get





> **POST** /alert-manager/v1/note/get
>






    
<br>

### list





> **POST** /alert-manager/v1/note/list
>






    
<br>

### stat





> **POST** /alert_manager/v1/note/stat
>






    


<br>
<br>

## Message



### NoteCreateRequest
* **alert_id** (string)   `Required` 

    
* **note** (string)   `Required` 

    <br>

### NoteInfo
* **note_id** (string)   `Required` 

    
* **note** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **service_id** (string)   `Required` 

    
* **alert_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **created_by** (string)   `Required` 

    <br>

### NoteRequest
* **note_id** (string)   `Required` 

    <br>

### NoteSearchQuery
* **query** (Query)  

    
* **workspace_id** (string)  

    
* **service_id** (string)  

    
* **alert_id** (string)  

    
* **note_id** (string)  

    
* **created_by** (string)  

    <br>

### NoteStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### NoteUpdateRequest
* **note_id** (string)   `Required` 

    
* **note** (string)  

    <br>

### NotesInfo
* **results** (NoteInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
