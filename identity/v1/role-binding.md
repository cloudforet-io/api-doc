---
description:  
---
# Role binding

>  **Package : spaceone.api.identity.v1**

## RoleBinding

{% hint style="info" %}
**RoleBinding Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](role-binding.md#create)|   [CreateRoleBindingRequest](role-binding.md#createrolebindingrequest) |   [RoleBindingInfo](role-binding.md#rolebindinginfo) |  |
| 2 | [**update**](role-binding.md#update)|   [UpdateRoleBindingRequest](role-binding.md#updaterolebindingrequest) |   [RoleBindingInfo](role-binding.md#rolebindinginfo) |  |
| 3 | [**delete**](role-binding.md#delete)|   [RoleBindingRequest](role-binding.md#rolebindingrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**get**](role-binding.md#get)|   [GetRoleBindingRequest](role-binding.md#getrolebindingrequest) |   [RoleBindingInfo](role-binding.md#rolebindinginfo) |  |
| 5 | [**list**](role-binding.md#list)|   [RoleBindingQuery](role-binding.md#rolebindingquery) |   [RoleBindingsInfo](role-binding.md#rolebindingsinfo) |  |
| 6 | [**stat**](role-binding.md#stat)|   [RoleBindingStatQuery](role-binding.md#rolebindingstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /identity/v1/role-bindings
>


| Type | Message |
| :--- | :--- |
| Request | [CreateRoleBindingRequest](role-binding.md#createrolebindingrequest) |
| Response |  [RoleBindingInfo](role-binding.md#rolebindinginfo)  |
 
 

 
### update
> **PUT** /identity/v1/role-bindings/{role_binding_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateRoleBindingRequest](role-binding.md#updaterolebindingrequest) |
| Response |  [RoleBindingInfo](role-binding.md#rolebindinginfo)  |
 
 

 
### delete
> **DELETE** /identity/v1/role-bindings/{role_binding_id}
>


| Type | Message |
| :--- | :--- |
| Request | [RoleBindingRequest](role-binding.md#rolebindingrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /identity/v1/role-bindings/{role_binding_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetRoleBindingRequest](role-binding.md#getrolebindingrequest) |
| Response |  [RoleBindingInfo](role-binding.md#rolebindinginfo)  |
 
 

 
### list
> **GET** /identity/v1/role-bindings
>
> **POST** /identity/v1/role-bindings/search



| Type | Message |
| :--- | :--- |
| Request | [RoleBindingQuery](role-binding.md#rolebindingquery) |
| Response |  [RoleBindingsInfo](role-binding.md#rolebindingsinfo)  |
 
 

 
### stat
> **POST** /identity/v1/roles/stat
>


| Type | Message |
| :--- | :--- |
| Request | [RoleBindingStatQuery](role-binding.md#rolebindingstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateRoleBindingRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | resource_type |string|✅| |
| 2 | resource_id |string|✅| |
| 3 | role_id |string|✅| |
| 4 | project_id |string|❌| |
| 5 | project_group_id |string|❌| |
| 6 | labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|❌| |
| 7 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 8 | domain_id |string|✅| |

### GetRoleBindingRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | role_binding_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### RoleBindingInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | role_binding_id |string | |
| 2 | resource_type |string | |
| 3 | resource_id |string | |
| 4 | role_info |[RoleInfo](role-binding.md#roleinfo) | |
| 5 | project_info |[ProjectInfo](role-binding.md#projectinfo) | |
| 6 | project_group_info |[ProjectGroupInfo](role-binding.md#projectgroupinfo) | |
| 7 | labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| 8 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 9 | domain_id |string | |
| 10 | created_at |string | |

### RoleBindingQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | role_binding_id |string|❌| |
| 3 | resource_type |string|❌| |
| 4 | resource_id |string|❌| |
| 5 | role_id |string|❌| |
| 6 | role_type |string|❌| |
| 7 | project_id |string|❌| |
| 8 | project_group_id |string|❌| |
| 9 | domain_id |string|✅| |

### RoleBindingRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | role_binding_id |string|✅| |
| 2 | domain_id |string|✅| |

### RoleBindingStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### RoleBindingsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of RoleBindingInfo](role-binding.md#rolebindinginfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateRoleBindingRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | role_binding_id |string|✅| |
| 2 | labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|❌| |
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | domain_id |string|✅| |
