---
description:  
---
# Provider

>  **Package : spaceone.api.repository.v2**

## Provider

{% hint style="info" %}
**Provider Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](provider.md#create)|   [CreateProviderRequest](provider.md#createproviderrequest) |   [ProviderInfo](provider.md#providerinfo) |
| [**update**](provider.md#update)|   [UpdateProviderRequest](provider.md#updateproviderrequest) |   [ProviderInfo](provider.md#providerinfo) |
| [**sync**](provider.md#sync)|   [ProviderRequest](provider.md#providerrequest) |   [ProviderInfo](provider.md#providerinfo) |
| [**delete**](provider.md#delete)|   [ProviderRequest](provider.md#providerrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](provider.md#get)|   [GetProviderRequest](provider.md#getproviderrequest) |   [ProviderInfo](provider.md#providerinfo) |
| [**list**](provider.md#list)|   [ProviderQuery](provider.md#providerquery) |   [ProvidersInfo](provider.md#providersinfo) | 
 

 
### create
> **POST** /repository/v2/provider/create
>


| Type | Message |
| :--- | :--- |
| Request | [CreateProviderRequest](provider.md#createproviderrequest) |
| Response |  [ProviderInfo](provider.md#providerinfo)  |
 
 

 
### update
> **POST** /repository/v2/provider/update
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateProviderRequest](provider.md#updateproviderrequest) |
| Response |  [ProviderInfo](provider.md#providerinfo)  |
 
 

 
### sync
> **POST** /repository/v2/provider/sync
>


| Type | Message |
| :--- | :--- |
| Request | [ProviderRequest](provider.md#providerrequest) |
| Response |  [ProviderInfo](provider.md#providerinfo)  |
 
 

 
### delete
> **POST** /repository/v2/provider/delete
>


| Type | Message |
| :--- | :--- |
| Request | [ProviderRequest](provider.md#providerrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **POST** /repository/v2/provider/get
>


| Type | Message |
| :--- | :--- |
| Request | [GetProviderRequest](provider.md#getproviderrequest) |
| Response |  [ProviderInfo](provider.md#providerinfo)  |
 
 

 
### list
> **POST** /repository/v2/providers/list
>


| Type | Message |
| :--- | :--- |
| Request | [ProviderQuery](provider.md#providerquery) |
| Response |  [ProvidersInfo](provider.md#providersinfo)  |


## 

## Message

### Capability
| Field | Type |  Description |
| :--- | :--- | :--- |
| trusted_service_account |string | |

### CreateProviderRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| provider |string|✔| |
| name |string|✔| |
| sync_mode |[SyncMode](provider.md#syncmode)|✘| |
| sync_options |[SyncOptions](provider.md#syncoptions)|✘| |
| description |[list of Description](provider.md#description)|✘| |
| schema |[list of ProviderSchema](provider.md#providerschema)|✘| |
| capability |[Capability](provider.md#capability)|✘| |
| color |string|✘| |
| icon |string|✘| |
| reference |[list of Reference](provider.md#reference)|✘| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✘| |

### Description
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource_type |string | |
| body |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### GetProviderRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| provider |string|✔| |
| only |list of string|✘| |
| domain_id |string|✘| |

### ProviderInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| provider |string | |
| name |string | |
| sync_mode |[SyncMode](provider.md#syncmode) | |
| sync_options |[SyncOptions](provider.md#syncoptions) | |
| description |[list of Description](provider.md#description) | |
| schema |[list of ProviderSchema](provider.md#providerschema) | |
| capability |[Capability](provider.md#capability) | |
| color |string | |
| icon |string | |
| reference |[list of Reference](provider.md#reference) | |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| remote_repository |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |
| created_at |string | |

### ProviderQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| provider |string|✘| |
| name |string|✘| |
| sync_mode |[SyncMode](provider.md#syncmode)|✘| |
| remote_repository_name |string|✘| |
| domain_id |string|✘| |

### ProviderRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| provider |string|✔| |
| domain_id |string|✘| |

### ProviderSchema
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource_type |string | |
| secret_type |string | |
| schema_id |string | |

### ProvidersInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ProviderInfo](provider.md#providerinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### Reference
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource_type |string | |
| link |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### UpdateProviderRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| provider |string|✔| |
| name |string|✘| |
| sync_mode |[SyncMode](provider.md#syncmode)|✘| |
| sync_options |[SyncOptions](provider.md#syncoptions)|✘| |
| description |[list of Description](provider.md#description)|✘| |
| schema |[list of ProviderSchema](provider.md#providerschema)|✘| |
| capability |[Capability](provider.md#capability)|✘| |
| color |string|✘| |
| icon |string|✘| |
| reference |[list of Reference](provider.md#reference)|✘| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✘| |
