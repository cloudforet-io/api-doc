---
title: "Note"
linkTitle: "Note"
weight: 3
bookFlatSection: true
---
# [Note](#Note)
A Note is a comment on an Event, and is used for incident management.


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

Creates a new Note. You can create Notes for each Alert to record the information needed to manage the Alerts.



> **POST** /monitoring/v1/note/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateNoteRequest](./Note#createnoterequest)

* **alert_id** (string)  `Required` 


* **note** (string)  `Required` 


* **domain_id** (string)  `Required` 





{{< highlight json >}}
{
   "alert_id": "alert-160ce04f6908",
   "note": "This is a description",
   "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NoteInfo](#NOTEINFO)
* **note_id** (string)  `Required` 

* **alert_id** (string)  `Required` 

* **note** (string)  `Required` 

* **created_by** (string)  `Required` 

* **project_id** (string)  `Required` 

* **domain_id** (string)  `Required` 

* **created_at** (string)  `Required` 



{{< highlight json >}}
{
   "note_id": "note-df107d31bf20",
   "alert_id": "alert-160ce04f6908",
   "note": "This is a description",
   "created_by": "seolmin@mz.co.kr",
   "project_id": "project-52a423012d5e",
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-06-29T08:26:14.418Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific Note. You must specify the `note_id` for Note validation check. If the Note exists, it is updated.



> **POST** /monitoring/v1/note/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateNoteRequest](./Note#updatenoterequest)

* **note_id** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **note** (string) 





{{< highlight json >}}
{
   "note_id": "note-df107d31bf20",
   "note": "This is a test",
   "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NoteInfo](#NOTEINFO)
* **note_id** (string)  `Required` 

* **alert_id** (string)  `Required` 

* **note** (string)  `Required` 

* **created_by** (string)  `Required` 

* **project_id** (string)  `Required` 

* **domain_id** (string)  `Required` 

* **created_at** (string)  `Required` 



{{< highlight json >}}
{
   "note_id": "note-df107d31bf20",
   "alert_id": "alert-160ce04f6908",
   "note": "This is a description",
   "created_by": "seolmin@mz.co.kr",
   "project_id": "project-52a423012d5e",
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-06-29T08:26:14.418Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific Note. You must specify the `note_id` of the Note to delete.



> **POST** /monitoring/v1/note/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[NoteRequest](./Note#noterequest)

* **note_id** (string)  `Required` 


* **domain_id** (string)  `Required` 





{{< highlight json >}}
{
   "note_id": "note-0bfac585bf5a",
   "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Note. You must specify the `note_id` and `domain_id`.



> **POST** /monitoring/v1/note/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetNoteRequest](./Note#getnoterequest)

* **note_id** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **only** (string) 





{{< highlight json >}}
{
   "note_id": "note-0bfac585bf5a",
   "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NoteInfo](#NOTEINFO)
* **note_id** (string)  `Required` 

* **alert_id** (string)  `Required` 

* **note** (string)  `Required` 

* **created_by** (string)  `Required` 

* **project_id** (string)  `Required` 

* **domain_id** (string)  `Required` 

* **created_at** (string)  `Required` 



{{< highlight json >}}
{
   "note_id": "note-df107d31bf20",
   "alert_id": "alert-160ce04f6908",
   "note": "This is a description",
   "created_by": "seolmin@mz.co.kr",
   "project_id": "project-52a423012d5e",
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-06-29T08:26:14.418Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Notes. You can use a query to get a filtered list of Notes.



> **POST** /monitoring/v1/note/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[NoteQuery](./Note#notequery)

* **query** (Query) 


* **note_id** (string) 


* **alert_id** (string) 


* **created_by** (string) 


* **project_id** (string) 


* **domain_id** (string) 





{{< highlight json >}}
{
   "query": {},
   "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NotesInfo](#NOTESINFO)
* **results** (NoteInfo)  `Required` 

* **total_count** (int32)  `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /monitoring/v1/note/stat
>






    


<br>
<br>

## Message



### CreateNoteRequest
* **alert_id** (string)  `Required` 

    
* **note** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### GetNoteRequest
* **note_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **only** (string) 

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
* **query** (Query) 

    
* **note_id** (string) 

    
* **alert_id** (string) 

    
* **created_by** (string) 

    
* **project_id** (string) 

    
* **domain_id** (string) 

    <br>

### NoteRequest
* **note_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### NoteStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### NotesInfo
* **results** (NoteInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateNoteRequest
* **note_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **note** (string) 

    <br>
