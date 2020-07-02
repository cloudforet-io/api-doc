---
description: null
---

# Project Group

> **Package : spaceone.api.identity.v1**

## ProjectGroup

{% hint style="info" %}
**ProjectGroup Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](project-group.md#create) | [CreateProjectGroupRequest](project-group.md#createprojectgrouprequest) | [ProjectGroupInfo](project-group.md#projectgroupinfo) |  |
| 2 | [update](project-group.md#update) | [UpdateProjectGroupRequest](project-group.md#updateprojectgrouprequest) | [ProjectGroupInfo](project-group.md#projectgroupinfo) |  |
| 3 | [delete](project-group.md#delete) | [ProjectGroupRequest](project-group.md#projectgrouprequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 4 | [add\_member](project-group.md#add_member) | [ProjectGroupMemberRequest](project-group.md#projectgroupmemberrequest) | [ProjectGroupMemberInfo](project-group.md#projectgroupmemberinfo) |  |
| 5 | [modify\_member](project-group.md#modify_member) | [ProjectGroupMemberRequest](project-group.md#projectgroupmemberrequest) | [ProjectGroupMemberInfo](project-group.md#projectgroupmemberinfo) |  |
| 6 | [remove\_member](project-group.md#remove_member) | [RemoveProjectGroupMemberRequest](project-group.md#removeprojectgroupmemberrequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 7 | [get](project-group.md#get) | [GetProjectGroupRequest](project-group.md#getprojectgrouprequest) | [ProjectGroupInfo](project-group.md#projectgroupinfo) |  |
| 8 | [list](project-group.md#list) | [ProjectGroupQuery](project-group.md#projectgroupquery) | [ProjectGroupsInfo](project-group.md#projectgroupsinfo) |  |
| 9 | [stat](project-group.md#stat) | [ProjectGroupStatQuery](project-group.md#projectgroupstatquery) | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |
| 10 | [list\_members](project-group.md#list_members) | [ProjectGroupMemberQuery](project-group.md#projectgroupmemberquery) | [ProjectGroupMembersInfo](project-group.md#projectgroupmembersinfo) |  |
| 11 | [list\_projects](project-group.md#list_projects) | [ProjectGroupProjectQuery](project-group.md#projectgroupprojectquery) | [ProjectGroupProjectsInfo](project-group.md#projectgroupprojectsinfo) |  |

### create

> **POST** /identity/v1/project-groups

| Type | Message |
| :--- | :--- |
| Request | [CreateProjectGroupRequest](project-group.md#createprojectgrouprequest) |
| Response | [ProjectGroupInfo](project-group.md#projectgroupinfo) |

### update

> **PUT** /identity/v1/project-group/{project\_group\_id}

| Type | Message |
| :--- | :--- |
| Request | [UpdateProjectGroupRequest](project-group.md#updateprojectgrouprequest) |
| Response | [ProjectGroupInfo](project-group.md#projectgroupinfo) |

### delete

> **DELETE** /identity/v1/project-group/{project\_id}

| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupRequest](project-group.md#projectgrouprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### add\_member

> **POST** /identity/v1/project-group/{project\_group\_id}/members

| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupMemberRequest](project-group.md#projectgroupmemberrequest) |
| Response | [ProjectGroupMemberInfo](project-group.md#projectgroupmemberinfo) |

### modify\_member

> **PUT** /identity/v1/project-group/{project\_group\_id}/member/{user\_id}

| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupMemberRequest](project-group.md#projectgroupmemberrequest) |
| Response | [ProjectGroupMemberInfo](project-group.md#projectgroupmemberinfo) |

### remove\_member

> **DELETE** /identity/v1/project-group/{project\_group\_id}/member/{user\_id}

| Type | Message |
| :--- | :--- |
| Request | [RemoveProjectGroupMemberRequest](project-group.md#removeprojectgroupmemberrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### get

> **GET** /identity/v1/project-group/{project\_group\_id}

| Type | Message |
| :--- | :--- |
| Request | [GetProjectGroupRequest](project-group.md#getprojectgrouprequest) |
| Response | [ProjectGroupInfo](project-group.md#projectgroupinfo) |

### list

> **GET** /identity/v1/project-groups
>
> **POST** /identity/v1/project-groups/search

| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupQuery](project-group.md#projectgroupquery) |
| Response | [ProjectGroupsInfo](project-group.md#projectgroupsinfo) |

### stat

> **POST** /identity/v1/project-groups/stat

| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupStatQuery](project-group.md#projectgroupstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |

### list\_members

> **GET** /identity/v1/project-group/{project\_group\_id}/members
>
> **POST** /identity/v1/project-group/{project\_id}/members/search

| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupMemberQuery](project-group.md#projectgroupmemberquery) |
| Response | [ProjectGroupMembersInfo](project-group.md#projectgroupmembersinfo) |

### list\_projects

> **GET** /identity/v1/project-group/{project\_group\_id}/projects
>
> **POST** /identity/v1/project-group/{project\_id}/projects/search

| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupProjectQuery](project-group.md#projectgroupprojectquery) |
| Response | [ProjectGroupProjectsInfo](project-group.md#projectgroupprojectsinfo) |

## Message

### CreateProjectGroupRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string | ✅ |  |
| 2 | parent\_project\_group\_id | string | ✅ |  |
| 3 | domain\_id | string | ✅ |  |
| 4 | template\_id | string | ❌ |  |
| 5 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ❌ |  |

### GetProjectGroupRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project\_group\_id | string | ✅ |  |
| 2 | domain\_id | string | ✅ |  |
| 3 | only | string | ❌ |  |

### ProjectGroupInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project\_group\_id | string |  |  |
| 2 | name | string |  |  |
| 3 | parent\_project\_group\_info | [ProjectGroupInfo](project-group.md#projectgroupinfo) |  | {'repeated Template fields = 3;                 // TODO': 'Not be implemented TEMPLATE yet', 'string template\_id = 4;                       // TODO': 'Not be implemented TEMPLATE yet'} |
| 4 | domain\_id | string |  |  |
| 5 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 6 | created\_by | string |  |  |
| 7 | created\_at | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  |  |
| 8 | deleted\_at | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  |  |

### ProjectGroupMemberInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project\_group\_info | [ProjectGroupInfo](project-group.md#projectgroupinfo) |  |  |
| 2 | user\_info | [UserInfo](project-group.md#userinfo) |  |  |
| 3 | roles | [RoleInfo](project-group.md#roleinfo) |  |  |
| 4 | labels | string |  |  |

### ProjectGroupMemberQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) | ❌ |  |
| 2 | project\_group\_id | string | ✅ |  |
| 3 | user\_id | string | ❌ |  |
| 4 | domain\_id | string | ✅ |  |

### ProjectGroupMemberRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project\_group\_id | string | ✅ |  |
| 2 | user\_id | string | ✅ |  |
| 3 | domain\_id | string | ✅ |  |
| 4 | roles | string | ✅ |  |
| 5 | labels | string | ✅ |  |

### ProjectGroupMembersInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [ProjectGroupMemberInfo](project-group.md#projectgroupmemberinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### ProjectGroupProjectInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project\_id | string |  |  |
| 2 | name | string |  |  |
| 3 | state | string |  |  |
| 4 | project\_group\_info | [ProjectGroupInfo](project-group.md#projectgroupinfo) |  | {'google.protobuf.Struct template\_data = 4; // TODO': 'Not be implemented template service yet'} |
| 5 | domain\_id | string |  |  |
| 6 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 7 | created\_by | string |  |  |
| 8 | created\_at | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  |  |
| 9 | deleted\_at | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  |  |

### ProjectGroupProjectQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) | ❌ |  |
| 2 | project\_group\_id | string | ✅ |  |
| 3 | recursive | bool | ❌ |  |
| 4 | domain\_id | string | ✅ |  |

### ProjectGroupProjectsInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [ProjectGroupProjectInfo](project-group.md#projectgroupprojectinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### ProjectGroupQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) | ❌ |  |
| 2 | project\_group\_id | string | ❌ |  |
| 3 | parent\_project\_group\_id | string | ❌ |  |
| 4 | name | string | ❌ |  |
| 5 | template\_id | string | ❌ |  |
| 6 | domain\_id | string | ✅ |  |

### ProjectGroupRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project\_group\_id | string | ✅ |  |
| 2 | domain\_id | string | ✅ |  |

### ProjectGroupStatQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) | ✅ |  |
| 2 | domain\_id | string | ✅ |  |

### ProjectGroupsInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [ProjectGroupInfo](project-group.md#projectgroupinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### RemoveProjectGroupMemberRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project\_group\_id | string | ✅ |  |
| 2 | user\_id | string | ✅ |  |
| 3 | domain\_id | string | ✅ |  |

### UpdateProjectGroupRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project\_group\_id | string | ✅ |  |
| 2 | parent\_project\_group\_id | string | ✅ |  |
| 3 | name | string | ❌ |  |
| 4 | release\_parent\_project\_group | bool | ❌ |  |
| 5 | domain\_id | string | ✅ |  |
| 6 | template\_id | string | ❌ |  |
| 7 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ❌ |  |

