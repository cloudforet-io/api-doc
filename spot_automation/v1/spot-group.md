---
description:  
---
# Spot group

>  **Package : spaceone.api.spot_automation.v1**

## SpotGroup

{% hint style="info" %}
**SpotGroup Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :--- | :--- | :--- | :--- |
| [**create**](spot-group.md#create)|   [CreateSpotGroupRequest](spot-group.md#createspotgrouprequest) |   [SpotGroupInfo](spot-group.md#spotgroupinfo) |  |
| [**update**](spot-group.md#update)|   [UpdateSpotGroupRequest](spot-group.md#updatespotgrouprequest) |   [SpotGroupInfo](spot-group.md#spotgroupinfo) |  |
| [**delete**](spot-group.md#delete)|   [SpotGroupRequest](spot-group.md#spotgrouprequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](spot-group.md#get)|   [GetSpotGroupRequest](spot-group.md#getspotgrouprequest) |   [SpotGroupInfo](spot-group.md#spotgroupinfo) |  |
| [**list**](spot-group.md#list)|   [QuerySpotGroupRequest](spot-group.md#queryspotgrouprequest) |   [SpotGroupsInfo](spot-group.md#spotgroupsinfo) |  |
| [**get_candidates**](spot-group.md#get_candidates)|   [GetCandidatesRequest](spot-group.md#getcandidatesrequest) |   [CandidatesInfo](spot-group.md#candidatesinfo) |  |
| [**stat**](spot-group.md#stat)|   [SpotGroupStatRequest](spot-group.md#spotgroupstatrequest) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /spot-automation/v1/spot-groups
>


| Type | Message |
| :--- | :--- |
| Request | [CreateSpotGroupRequest](spot-group.md#createspotgrouprequest) |
| Response |  [SpotGroupInfo](spot-group.md#spotgroupinfo)  |
 
 

 
### update
> **PUT** /spot-automation/v1/spot-group/{spot_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateSpotGroupRequest](spot-group.md#updatespotgrouprequest) |
| Response |  [SpotGroupInfo](spot-group.md#spotgroupinfo)  |
 
 

 
### delete
> **DELETE** /spot-automation/v1/spot-group/{spot_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [SpotGroupRequest](spot-group.md#spotgrouprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /spot-automation/v1/spot-group/{spot_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetSpotGroupRequest](spot-group.md#getspotgrouprequest) |
| Response |  [SpotGroupInfo](spot-group.md#spotgroupinfo)  |
 
 

 
### list
> **GET** /spot-automation/v1/spot-groups
>
> **POST** /spot-automation/v1/spot-groups/search



| Type | Message |
| :--- | :--- |
| Request | [QuerySpotGroupRequest](spot-group.md#queryspotgrouprequest) |
| Response |  [SpotGroupsInfo](spot-group.md#spotgroupsinfo)  |
 
 

 
### get_candidates
> **GET** /spot-automation/v1/spot-group/candidates
>


| Type | Message |
| :--- | :--- |
| Request | [GetCandidatesRequest](spot-group.md#getcandidatesrequest) |
| Response |  [CandidatesInfo](spot-group.md#candidatesinfo)  |
 
 

 
### stat
> **POST** /spot-automation/v1/spot-groups/stat
>


| Type | Message |
| :--- | :--- |
| Request | [SpotGroupStatRequest](spot-group.md#spotgroupstatrequest) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CandidateInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| type |string | |
| priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CandidatesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CandidateInfo](spot-group.md#candidateinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateSpotGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| resource_id |string|✅| |
| resource_type |string|✅| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| user_id |string|✅| |
| domain_id |string|✅| |

### GetCandidatesRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_id |string|✅| |
| resource_type |string|✅| |
| limit |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✅| |
| domain_id |string|✅| |

### GetSpotGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| spot_group_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### QuerySpotGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| spot_group_id |string|❌| |
| name |string|❌| |
| resource_id |string|❌| |
| resource_type |string|❌| |
| provider |string|❌| |
| project_id |string|❌| |
| region_code |string|❌| |
| domain_id |string|✅| |

### SpotGroupInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| spot_group_id |string | |
| name |string | |
| resource_id |string | |
| resource_type |string | |
| region_code |string | |
| provider |string | |
| cloud_service_group |string | |
| cloud_service_type |string | |
| reference |[SpotGroupResourceReference](spot-group.md#spotgroupresourcereference) | |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| project_id |string | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |
| created_by |string | |
| created_at |string | |

### SpotGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| spot_group_id |string|✅| |
| domain_id |string|✅| |

### SpotGroupResourceReference
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource_id |string | |
| external_link |string | |

### SpotGroupStatRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### SpotGroupsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of SpotGroupInfo](spot-group.md#spotgroupinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateSpotGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| spot_group_id |string|✅| |
| name |string|❌| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |
