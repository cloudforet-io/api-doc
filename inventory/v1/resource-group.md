---
description:  
---
# Resource group

>  **Package : spaceone.api.inventory.v1**

## ResourceGroup

{% hint style="info" %}
**ResourceGroup Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](resource-group.md#create)|   [CreateResourceGroupRequest](resource-group.md#createresourcegrouprequest) |   [ResourceGroupInfo](resource-group.md#resourcegroupinfo) |  |
| 2 | [**update**](resource-group.md#update)|   [UpdateResourceGroupRequest](resource-group.md#updateresourcegrouprequest) |   [ResourceGroupInfo](resource-group.md#resourcegroupinfo) |  |
| 3 | [**delete**](resource-group.md#delete)|   [ResourceGroupRequest](resource-group.md#resourcegrouprequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**get**](resource-group.md#get)|   [GetResourceGroupRequest](resource-group.md#getresourcegrouprequest) |   [ResourceGroupInfo](resource-group.md#resourcegroupinfo) |  |
| 5 | [**list**](resource-group.md#list)|   [ResourceGroupQuery](resource-group.md#resourcegroupquery) |   [ResourceGroupsInfo](resource-group.md#resourcegroupsinfo) |  |
| 6 | [**stat**](resource-group.md#stat)|   [ResourceGroupStatQuery](resource-group.md#resourcegroupstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /inventory/v1/resource-groups
>


| Type | Message |
| :--- | :--- |
| Request | [CreateResourceGroupRequest](resource-group.md#createresourcegrouprequest) |
| Response |  [ResourceGroupInfo](resource-group.md#resourcegroupinfo)  |
 
 

 
### update
> **PUT** /inventory/v1/resource-group/{resource_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateResourceGroupRequest](resource-group.md#updateresourcegrouprequest) |
| Response |  [ResourceGroupInfo](resource-group.md#resourcegroupinfo)  |
 
 

 
### delete
> **DELETE** /inventory/v1/resource-group/{resource_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ResourceGroupRequest](resource-group.md#resourcegrouprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /inventory/v1/resource-group/{resource_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetResourceGroupRequest](resource-group.md#getresourcegrouprequest) |
| Response |  [ResourceGroupInfo](resource-group.md#resourcegroupinfo)  |
 
 

 
### list
> **GET** /inventory/v1/resource-groups
>
> **POST** /inventory/v1/resource-groups/search



| Type | Message |
| :--- | :--- |
| Request | [ResourceGroupQuery](resource-group.md#resourcegroupquery) |
| Response |  [ResourceGroupsInfo](resource-group.md#resourcegroupsinfo)  |
 
 

 
### stat
> **POST** /inventory/v1/resource-groups/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ResourceGroupStatQuery](resource-group.md#resourcegroupstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateResourceGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | resources |[Resource](resource-group.md#resource)|✅| |
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | project_id |string|✅| |
| 5 | domain_id |string|✅| |

### GetResourceGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource_group_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### Resource
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource_type |string|✅| |
| 2 | filter |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✅| |

### ResourceGroupInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | resource_group_id |string | |
| 2 | name |string | |
| 3 | resources |[Resource](resource-group.md#resource) | |
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 5 | project_id |string | |
| 6 | domain_id |string | |
| 7 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |

### ResourceGroupQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | resource_group_id |string|❌| |
| 3 | name |string|❌| |
| 4 | project_id |string|❌| |
| 5 | domain_id |string|✅| |

### ResourceGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource_group_id |string|✅| |
| 2 | domain_id |string|✅| |

### ResourceGroupStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### ResourceGroupsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[ResourceGroupInfo](resource-group.md#resourcegroupinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateResourceGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource_group_id |string|✅| |
| 2 | name |string|❌| |
| 3 | resources |[Resource](resource-group.md#resource)|❌| |
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 5 | release_project |bool|❌| |
| 6 | project_id |string|❌| |
| 7 | domain_id |string|✅| |
