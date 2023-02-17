---
description:  
---
# Role binding

>  **Package : spaceone.api.identity.v1**

## RoleBinding

{% hint style="info" %}
**RoleBinding Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](role-binding.md#create)|   [CreateRoleBindingRequest](role-binding.md#createrolebindingrequest) |   [RoleBindingInfo](role-binding.md#rolebindinginfo) |
| [**update**](role-binding.md#update)|   [UpdateRoleBindingRequest](role-binding.md#updaterolebindingrequest) |   [RoleBindingInfo](role-binding.md#rolebindinginfo) |
| [**delete**](role-binding.md#delete)|   [RoleBindingRequest](role-binding.md#rolebindingrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](role-binding.md#get)|   [GetRoleBindingRequest](role-binding.md#getrolebindingrequest) |   [RoleBindingInfo](role-binding.md#rolebindinginfo) |
| [**list**](role-binding.md#list)|   [RoleBindingQuery](role-binding.md#rolebindingquery) |   [RoleBindingsInfo](role-binding.md#rolebindingsinfo) |
| [**stat**](role-binding.md#stat)|   [RoleBindingStatQuery](role-binding.md#rolebindingstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /identity/v1/role-binding/create
>


| Type | Message |
| :--- | :--- |
| Request | [CreateRoleBindingRequest](role-binding.md#createrolebindingrequest) |
| Response |  [RoleBindingInfo](role-binding.md#rolebindinginfo)  |
 
 

 
### update
> **POST** /identity/v1/role-binding/update
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateRoleBindingRequest](role-binding.md#updaterolebindingrequest) |
| Response |  [RoleBindingInfo](role-binding.md#rolebindinginfo)  |
 
 

 
### delete
> **POST** /identity/v1/role-binding/delete
>


| Type | Message |
| :--- | :--- |
| Request | [RoleBindingRequest](role-binding.md#rolebindingrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **POST** /identity/v1/role-binding/get
>


| Type | Message |
| :--- | :--- |
| Request | [GetRoleBindingRequest](role-binding.md#getrolebindingrequest) |
| Response |  [RoleBindingInfo](role-binding.md#rolebindinginfo)  |
 
 

 
### list
> **POST** /identity/v1/role-binding/list
>


| Type | Message |
| :--- | :--- |
| Request | [RoleBindingQuery](role-binding.md#rolebindingquery) |
| Response |  [RoleBindingsInfo](role-binding.md#rolebindingsinfo)  |
 
 

 
### stat
> **POST** /identity/v1/role-binding/stat
>


| Type | Message |
| :--- | :--- |
| Request | [RoleBindingStatQuery](role-binding.md#rolebindingstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateRoleBindingRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_type |string|✔| |
| resource_id |string|✔| |
| role_id |string|✔| |
| project_id |string|✘| |
| project_group_id |string|✘| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |

### GetRoleBindingRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| role_binding_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### RoleBindingInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| role_binding_id |string | |
| resource_type |string | |
| resource_id |string | |
| role_info |[RoleInfo](role-binding.md#roleinfo) | |
| project_info |[ProjectInfo](role-binding.md#projectinfo) | |
| project_group_info |[ProjectGroupInfo](role-binding.md#projectgroupinfo) | |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |
| created_at |string | |

### RoleBindingQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| role_binding_id |string|✘| |
| resource_type |string|✘| |
| resource_id |string|✘| |
| role_id |string|✘| |
| role_type |string|✘| |
| project_id |string|✘| |
| project_group_id |string|✘| |
| domain_id |string|✔| |

### RoleBindingRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| role_binding_id |string|✔| |
| domain_id |string|✔| |

### RoleBindingStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### RoleBindingsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of RoleBindingInfo](role-binding.md#rolebindinginfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateRoleBindingRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| role_binding_id |string|✔| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
