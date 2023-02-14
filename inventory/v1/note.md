---
description:  
---
# Note

>  **Package : spaceone.api.inventory.v1**

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
> **POST** /inventory/v1/note/create
>

> ''

| Type | Message |
| :--- | :--- |
| Request | [CreateNoteRequest](note.md#createnoterequest) |
| Response |  [NoteInfo](note.md#noteinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **POST** /inventory/v1/note/update
>

> ''

| Type | Message |
| :--- | :--- |
| Request | [UpdateNoteRequest](note.md#updatenoterequest) |
| Response |  [NoteInfo](note.md#noteinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **POST** /inventory/v1/note/delete
>

> ''

| Type | Message |
| :--- | :--- |
| Request | [NoteRequest](note.md#noterequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** /inventory/v1/note/get
>

> ''

| Type | Message |
| :--- | :--- |
| Request | [GetNoteRequest](note.md#getnoterequest) |
| Response |  [NoteInfo](note.md#noteinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** /inventory/v1/note/list
>

> ''

| Type | Message |
| :--- | :--- |
| Request | [NoteQuery](note.md#notequery) |
| Response |  [NotesInfo](note.md#notesinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /inventory/v1/note/stat
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
| record_id |string|✔| |
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
| record_id |string | |
| cloud_service_id |string | |
| note |string | |
| created_by |string | |
| domain_id |string | |
| created_at |string | |

### NoteQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| note_id |string|✘| |
| record_id |string|✘| |
| cloud_service_id |string|✘| |
| created_by |string|✘| |
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
