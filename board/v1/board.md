---
description: A Board is a bulletin-board-type resource for posting notices and announcements in Cloudforet.
---
# Board

>  **Package : spaceone.api.board.v1**

## Board

{% hint style="info" %}
**Board Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](board.md#create)|   [CreateBoardRequest](board.md#createboardrequest) |   [BoardInfo](board.md#boardinfo) |
| [**update**](board.md#update)|   [UpdateBoardRequest](board.md#updateboardrequest) |   [BoardInfo](board.md#boardinfo) |
| [**set_categories**](board.md#set_categories)|   [SetBoardCategoriesRequest](board.md#setboardcategoriesrequest) |   [BoardInfo](board.md#boardinfo) |
| [**delete**](board.md#delete)|   [BoardRequest](board.md#boardrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](board.md#get)|   [GetBoardRequest](board.md#getboardrequest) |   [BoardInfo](board.md#boardinfo) |
| [**list**](board.md#list)|   [BoardQuery](board.md#boardquery) |   [BoardsInfo](board.md#boardsinfo) |
| [**stat**](board.md#stat)|   [BoardStatQuery](board.md#boardstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /board/v1/boards
>

> Creates a new Board with SYSTEM permission. The `name` of the board is only required. You can add one or more `categories` representing the Board's attributes.

| Type | Message |
| :--- | :--- |
| Request | [CreateBoardRequest](board.md#createboardrequest) |
| Response |  [BoardInfo](board.md#boardinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "notice",
    "categories": [
        "admin",
        "developer",
        "devops"
    ],
    "tags": {
        "a": "b"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "board_id": "board-123456789012",
    "name": "notice",
    "categories": [
        "admin",
        "developer",
        "devops"
    ],
    "tags": {
        "a": "b"
    },
    "created_at": "2022-01-01T06:47:27.759Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **PUT** /board/v1/board/{board_id}
>

> Updates a specific Board with SYSTEM permission. You can make changes in Board settings, including `name` and `tags`.

| Type | Message |
| :--- | :--- |
| Request | [UpdateBoardRequest](board.md#updateboardrequest) |
| Response |  [BoardInfo](board.md#boardinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "board_id": "board-123456789012",
    "name": "system notice",
    "tags": {
        "b": "c"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "board_id": "board-123456789012",
    "name": "system notice",
    "categories": [
        "admin",
        "developer",
        "devops"
    ],
    "tags": {
        "b": "c"
    },
    "created_at": "2022-01-01T06:47:27.759Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### set_categories
> **PUT** /board/v1/board/{board_id}/set-categories
>

> Adds or changes `categories` of a specific Board with SYSTEM permission. A change in `categories` of a Board does not affect the `category` of the child Posts.

| Type | Message |
| :--- | :--- |
| Request | [SetBoardCategoriesRequest](board.md#setboardcategoriesrequest) |
| Response |  [BoardInfo](board.md#boardinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "board_id": "board-123456789012",
    "categories": [
        "Developer",
        "SRE",
        "Devops"
    ]
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "board_id": "board-123456789012",
    "name": "dev-notice",
    "categories": [
        "Developer",
        "SRE",
        "Devops"
    ],
    "tags": {
        "b": "c"
    },
    "created_at": "2022-01-01T05:24:19.758Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **DELETE** /board/v1/board/{board_id}
>

> Deletes a specific Board with `SYSTEM` permission. You can delete a Board regardless of the presence of Posts created under the Board.

| Type | Message |
| :--- | :--- |
| Request | [BoardRequest](board.md#boardrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "board_id": "board-123456789012"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /board/v1/board/{board_id}
>

> Gets a specific Board. You must specify the `board_id` of the Board to get. Prints detailed information about the Board, including `name`, `categories`.

| Type | Message |
| :--- | :--- |
| Request | [GetBoardRequest](board.md#getboardrequest) |
| Response |  [BoardInfo](board.md#boardinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "board_id": "board-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "board_id": "board-123456789012",
    "name": "dev-notice",
    "categories": [
        "Developer",
        "SRE",
        "Devops"
    ],
    "tags": {
        "b": "c"
    },
    "created_at": "2022-01-01T05:24:19.758Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /board/v1/boards
>
> **POST** /board/v1/boards/search


> Gets a list of all Boards. You can use a query to get a filtered list of Boards.

| Type | Message |
| :--- | :--- |
| Request | [BoardQuery](board.md#boardquery) |
| Response |  [BoardsInfo](board.md#boardsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {}
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "board_id": "board-123456789012",
            "name": "dev-notice",
            "categories": [
                "flower",
                "school",
                "spaceone"
            ],
            "tags": {
                "b": "c"
            },
            "created_at": "2022-01-01T05:16:08.549Z"
        },
        {
            "board_id": "board-987654321098",
            "name": "notice",
            "tags": {
                "a": "b"
            },
            "created_at": "2022-01-01T05:24:19.758Z"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /board/v1/boards/stat
>


| Type | Message |
| :--- | :--- |
| Request | [BoardStatQuery](board.md#boardstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### BoardInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| board_id |string | |
| name |string | |
| categories |list of string | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| created_at |string | |

### BoardQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✘| |
| name |string|✘| |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |

### BoardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✔| |

### BoardStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |

### BoardsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of BoardInfo](board.md#boardinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateBoardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |
| categories |list of string|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |

### GetBoardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✔| |
| only |list of string|✘| |

### SetBoardCategoriesRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✔| |
| categories |list of string|✘| |

### UpdateBoardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✔| |
| name |string|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
