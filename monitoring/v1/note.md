---
description: A Note is a comment on an Event, and is used for incident management.
---
# Note

>  **Package : spaceone.api.monitoring.v1**

## Note

{% hint style="info" %}
**Note Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](note.md#create)|   [CreateNoteRequest](note.md#createnoterequest) |   [NoteInfo](note.md#noteinfo) |
| [**update**](note.md#update)|   [UpdateNoteRequest](note.md#updatenoterequest) |   [NoteInfo](note.md#noteinfo) |
| [**delete**](note.md#delete)|   [NoteRequest](note.md#noterequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](note.md#get)|   [GetNoteRequest](note.md#getnoterequest) |   [NoteInfo](note.md#noteinfo) |
| [**list**](note.md#list)|   [NoteQuery](note.md#notequery) |   [NotesInfo](note.md#notesinfo) |
| [**stat**](note.md#stat)|   [NoteStatQuery](note.md#notestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /monitoring/v1/note/create
>

> Creates a new Note. You can create Notes for each Alert to record the information needed to manage the Alerts.

| Type | Message |
| :--- | :--- |
| Request | [CreateNoteRequest](note.md#createnoterequest) |
| Response |  [NoteInfo](note.md#noteinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "alert_id": "alert-160ce04f6908",
    "note": "This is a description",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "note_id": "note-df107d31bf20",
    "alert_id": "alert-160ce04f6908",
    "note": "This is a description",
    "created_by": "seolmin@mz.co.kr",
    "project_id": "project-52a423012d5e",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-06-29T08:26:14.418Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **POST** /monitoring/v1/note/update
>

> Updates a specific Note. You must specify the `note_id` for Note validation check. If the Note exists, it is updated.

| Type | Message |
| :--- | :--- |
| Request | [UpdateNoteRequest](note.md#updatenoterequest) |
| Response |  [NoteInfo](note.md#noteinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "note_id": "note-df107d31bf20",
    "note": "This is a test",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "note_id": "note-df107d31bf20",
    "alert_id": "alert-160ce04f6908",
    "note": "This is a test",
    "created_by": "seolmin@mz.co.kr",
    "project_id": "project-52a423012d5e",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-06-29T08:26:14.418Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **POST** /monitoring/v1/note/delete
>

> Deletes a specific Note. You must specify the `note_id` of the Note to delete.

| Type | Message |
| :--- | :--- |
| Request | [NoteRequest](note.md#noterequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "note_id": "note-0bfac585bf5a",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** /monitoring/v1/note/get
>

> Gets a specific Note. You must specify the `note_id` and `domain_id`.

| Type | Message |
| :--- | :--- |
| Request | [GetNoteRequest](note.md#getnoterequest) |
| Response |  [NoteInfo](note.md#noteinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "note_id": "note-0bfac585bf5a",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "note_id": "note-0bfac585bf5a",
    "alert_id": "alert-fbfd78e43df8",
    "note": "test",
    "created_by": "hykang@mz.co.kr",
    "project_id": "project-52a423012d5e",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-06-23T09:52:42.251Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** /monitoring/v1/note/list
>

> Gets a list of all Notes. You can use a query to get a filtered list of Notes.

| Type | Message |
| :--- | :--- |
| Request | [NoteQuery](note.md#notequery) |
| Response |  [NotesInfo](note.md#notesinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {},
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /monitoring/v1/note/stat
>


| Type | Message |
| :--- | :--- |
| Request | [NoteStatQuery](note.md#notestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateNoteRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✔| |
| note |string|✔| |
| domain_id |string|✔| |

### GetNoteRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| note_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### NoteInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| note_id |string | |
| alert_id |string | |
| note |string | |
| created_by |string | |
| project_id |string | |
| domain_id |string | |
| created_at |string | |

### NoteQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| note_id |string|✘| |
| alert_id |string|✘| |
| created_by |string|✘| |
| project_id |string|✘| |
| domain_id |string|✘| |

### NoteRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| note_id |string|✔| |
| domain_id |string|✔| |

### NoteStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### NotesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of NoteInfo](note.md#noteinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateNoteRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| note_id |string|✔| |
| note |string|✘| |
| domain_id |string|✔| |
