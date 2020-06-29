---
description:  
---
# Project

>  **Package : spaceone.api.identity.v1**

## Project

{% hint style="info" %}
**Project Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Project.md#create)| [CreateProjectRequest](Project.md#createprojectrequest) | [ProjectInfo](Project.md#projectinfo) |  |
| 2 | [update](Project.md#update)| [UpdateProjectRequest](Project.md#updateprojectrequest) | [ProjectInfo](Project.md#projectinfo) |  |
| 3 | [delete](Project.md#delete)| [ProjectRequest](Project.md#projectrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [add_member](Project.md#add_member)| [ProjectMemberRequest](Project.md#projectmemberrequest) | [ProjectMemberInfo](Project.md#projectmemberinfo) |  |
| 5 | [modify_member](Project.md#modify_member)| [ProjectMemberRequest](Project.md#projectmemberrequest) | [ProjectMemberInfo](Project.md#projectmemberinfo) |  |
| 6 | [remove_member](Project.md#remove_member)| [RemoveProjectMemberRequest](Project.md#removeprojectmemberrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 7 | [get](Project.md#get)| [GetProjectRequest](Project.md#getprojectrequest) | [ProjectInfo](Project.md#projectinfo) |  |
| 8 | [list](Project.md#list)| [ProjectQuery](Project.md#projectquery) | [ProjectsInfo](Project.md#projectsinfo) |  |
| 9 | [stat](Project.md#stat)| [ProjectStatQuery](Project.md#projectstatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |
| 10 | [list_members](Project.md#list_members)| [ProjectMemberQuery](Project.md#projectmemberquery) | [ProjectMembersInfo](Project.md#projectmembersinfo) |  |

### create
> **POST** /identity/v1/projects
>



| Type | Message |
| :--- | :--- |
| Request | [CreateProjectRequest](Project.md#createprojectrequest) |
| Response |  [ProjectInfo](Project.md#projectinfo)  |



### update
> **PUT** /identity/v1/project/{project_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateProjectRequest](Project.md#updateprojectrequest) |
| Response |  [ProjectInfo](Project.md#projectinfo)  |



### delete
> **DELETE** /identity/v1/project/{project_id}
>



| Type | Message |
| :--- | :--- |
| Request | [ProjectRequest](Project.md#projectrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### add_member
> **POST** /identity/v1/project/{project_id}/members
>



| Type | Message |
| :--- | :--- |
| Request | [ProjectMemberRequest](Project.md#projectmemberrequest) |
| Response |  [ProjectMemberInfo](Project.md#projectmemberinfo)  |



### modify_member
> **PUT** /identity/v1/project/{project_id}/member/{user_id}
>



| Type | Message |
| :--- | :--- |
| Request | [ProjectMemberRequest](Project.md#projectmemberrequest) |
| Response |  [ProjectMemberInfo](Project.md#projectmemberinfo)  |



### remove_member
> **DELETE** /identity/v1/project/{project_id}/member/{user_id}
>



| Type | Message |
| :--- | :--- |
| Request | [RemoveProjectMemberRequest](Project.md#removeprojectmemberrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /identity/v1/project/{project_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetProjectRequest](Project.md#getprojectrequest) |
| Response |  [ProjectInfo](Project.md#projectinfo)  |



### list
> **GET** /identity/v1/projects
>
> **POST** /identity/v1/projects/search




| Type | Message |
| :--- | :--- |
| Request | [ProjectQuery](Project.md#projectquery) |
| Response |  [ProjectsInfo](Project.md#projectsinfo)  |



### stat
> **POST** /identity/v1/projects/stat
>



| Type | Message |
| :--- | :--- |
| Request | [ProjectStatQuery](Project.md#projectstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |



### list_members
> **GET** /identity/v1/project/{project_id}/members
>
> **POST** /identity/v1/project/{project_id}/members/search




| Type | Message |
| :--- | :--- |
| Request | [ProjectMemberQuery](Project.md#projectmemberquery) |
| Response |  [ProjectMembersInfo](Project.md#projectmembersinfo)  |





## Message

### CreateProjectRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string | |required|
| 2 | project_group_id |string | |required|
| 3 | domain_id |string | |required|
| 4 | template_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |optional|
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |optional|

### GetProjectRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string | |required|
| 2 | domain_id |string | |required|
| 3 | only |string | |optional|

### ProjectInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string | ||
| 2 | name |string | ||
| 3 | state |string | ||
| 4 | project_group_info |[ProjectGroupInfo](Project.md#projectgroupinfo) | |{'google.protobuf.Struct template_data = 4; // TODO': 'Not be implemented template service yet'}|
| 5 | domain_id |string | ||
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 7 | created_by |string | ||
| 8 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||
| 9 | deleted_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### ProjectMemberInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_info |[ProjectInfo](Project.md#projectinfo) | ||
| 2 | user_info |[UserInfo](Project.md#userinfo) | ||
| 3 | roles |[RoleInfo](Project.md#roleinfo) | ||
| 4 | labels |string | ||

### ProjectMemberQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) | |optional|
| 2 | project_id |string | |required|
| 3 | domain_id |string | |required|
| 4 | user_id |string | |optional|

### ProjectMemberRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string | |required|
| 2 | user_id |string | |required|
| 3 | domain_id |string | |required|
| 4 | roles |string | |required|
| 5 | labels |string | |required|

### ProjectMembersInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[ProjectMemberInfo](Project.md#projectmemberinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### ProjectQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) | |optional|
| 2 | project_id |string | |optional|
| 3 | project_group_id |string | |optional|
| 4 | domain_id |string | |required|
| 5 | name |string | |optional|

### ProjectRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string | |required|
| 2 | domain_id |string | |required|

### ProjectStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) | |required|
| 2 | domain_id |string | |required|

### ProjectsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[ProjectInfo](Project.md#projectinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### RemoveProjectMemberRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string | |required|
| 2 | user_id |string | |required|
| 3 | domain_id |string | |required|

### UpdateProjectRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string | |required|
| 2 | project_group_id |string | |optional|
| 3 | name |string | |optional|
| 4 | domain_id |string | |required|
| 5 | template_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |optional|
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |optional|
