---
description:  
---
# Role binding

>  **Package : spaceone.api.identity.v1**

## RoleBinding

{% hint style="info" %}
**RoleBinding Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](role-binding.md#create)|   [CreateRoleBindingRequest](role-binding.md#createrolebindingrequest) |   [RoleBindingInfo](role-binding.md#rolebindinginfo) |  |
| [**update**](role-binding.md#update)|   [UpdateRoleBindingRequest](role-binding.md#updaterolebindingrequest) |   [RoleBindingInfo](role-binding.md#rolebindinginfo) |  |
| [**delete**](role-binding.md#delete)|   [RoleBindingRequest](role-binding.md#rolebindingrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](role-binding.md#get)|   [GetRoleBindingRequest](role-binding.md#getrolebindingrequest) |   [RoleBindingInfo](role-binding.md#rolebindinginfo) |  |
| [**list**](role-binding.md#list)|   [RoleBindingQuery](role-binding.md#rolebindingquery) |   [RoleBindingsInfo](role-binding.md#rolebindingsinfo) |  |
| [**stat**](role-binding.md#stat)|   [RoleBindingStatQuery](role-binding.md#rolebindingstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](role-binding.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateRoleBindingRequest](role-binding.md#createrolebindingrequest)  </div> | <div style="width:200px; text-align:center;">   [RoleBindingInfo](role-binding.md#rolebindinginfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](role-binding.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateRoleBindingRequest](role-binding.md#updaterolebindingrequest)  </div> | <div style="width:200px; text-align:center;">   [RoleBindingInfo](role-binding.md#rolebindinginfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](role-binding.md#delete) </div> | <div style="width:200px; text-align:center;">    [RoleBindingRequest](role-binding.md#rolebindingrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](role-binding.md#get) </div> | <div style="width:200px; text-align:center;">    [GetRoleBindingRequest](role-binding.md#getrolebindingrequest)  </div> | <div style="width:200px; text-align:center;">   [RoleBindingInfo](role-binding.md#rolebindinginfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](role-binding.md#list) </div> | <div style="width:200px; text-align:center;">    [RoleBindingQuery](role-binding.md#rolebindingquery)  </div> | <div style="width:200px; text-align:center;">   [RoleBindingsInfo](role-binding.md#rolebindingsinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](role-binding.md#stat) </div> | <div style="width:200px; text-align:center;">    [RoleBindingStatQuery](role-binding.md#rolebindingstatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
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
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_type |string|✅| |
| resource_id |string|✅| |
| role_id |string|✅| |
| project_id |string|❌| |
| project_group_id |string|❌| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### GetRoleBindingRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| role_binding_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

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
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| role_binding_id |string|❌| |
| resource_type |string|❌| |
| resource_id |string|❌| |
| role_id |string|❌| |
| role_type |string|❌| |
| project_id |string|❌| |
| project_group_id |string|❌| |
| domain_id |string|✅| |

### RoleBindingRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| role_binding_id |string|✅| |
| domain_id |string|✅| |

### RoleBindingStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### RoleBindingsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of RoleBindingInfo](role-binding.md#rolebindinginfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateRoleBindingRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| role_binding_id |string|✅| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |
