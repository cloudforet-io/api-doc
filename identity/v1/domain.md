---
description:  
---
# Domain

>  **Package : spaceone.api.identity.v1**

## Domain

{% hint style="info" %}
**Domain Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](domain.md#create)|   [CreateDomainRequest](domain.md#createdomainrequest) |   [DomainInfo](domain.md#domaininfo) |  |
| [**update**](domain.md#update)|   [UpdateDomainRequest](domain.md#updatedomainrequest) |   [DomainInfo](domain.md#domaininfo) |  |
| [**change_auth_plugin**](domain.md#change_auth_plugin)|   [ChangeAuthRequest](domain.md#changeauthrequest) |   [DomainInfo](domain.md#domaininfo) |  |
| [**update_plugin**](domain.md#update_plugin)|   [UpdatePluginRequest](domain.md#updatepluginrequest) |   [DomainInfo](domain.md#domaininfo) |  |
| [**verify_plugin**](domain.md#verify_plugin)|   [DomainRequest](domain.md#domainrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**delete**](domain.md#delete)|   [DomainRequest](domain.md#domainrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**enable**](domain.md#enable)|   [DomainRequest](domain.md#domainrequest) |   [DomainInfo](domain.md#domaininfo) |  |
| [**disable**](domain.md#disable)|   [DomainRequest](domain.md#domainrequest) |   [DomainInfo](domain.md#domaininfo) |  |
| [**get**](domain.md#get)|   [GetDomainRequest](domain.md#getdomainrequest) |   [DomainInfo](domain.md#domaininfo) |  |
| [**list**](domain.md#list)|   [DomainQuery](domain.md#domainquery) |   [DomainsInfo](domain.md#domainsinfo) |  |
| [**stat**](domain.md#stat)|   [DomainStatQuery](domain.md#domainstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |
| [**get_public_key**](domain.md#get_public_key)| .spaceone.api.core.v1.AuthenticationRequest|  .spaceone.api.core.v1.AuthenticationResponse|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](domain.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateDomainRequest](domain.md#createdomainrequest)  </div> | <div style="width:200px; text-align:center;">   [DomainInfo](domain.md#domaininfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](domain.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateDomainRequest](domain.md#updatedomainrequest)  </div> | <div style="width:200px; text-align:center;">   [DomainInfo](domain.md#domaininfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**change_auth_plugin**](domain.md#change_auth_plugin) </div> | <div style="width:200px; text-align:center;">    [ChangeAuthRequest](domain.md#changeauthrequest)  </div> | <div style="width:200px; text-align:center;">   [DomainInfo](domain.md#domaininfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update_plugin**](domain.md#update_plugin) </div> | <div style="width:200px; text-align:center;">    [UpdatePluginRequest](domain.md#updatepluginrequest)  </div> | <div style="width:200px; text-align:center;">   [DomainInfo](domain.md#domaininfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**verify_plugin**](domain.md#verify_plugin) </div> | <div style="width:200px; text-align:center;">    [DomainRequest](domain.md#domainrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](domain.md#delete) </div> | <div style="width:200px; text-align:center;">    [DomainRequest](domain.md#domainrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**enable**](domain.md#enable) </div> | <div style="width:200px; text-align:center;">    [DomainRequest](domain.md#domainrequest)  </div> | <div style="width:200px; text-align:center;">   [DomainInfo](domain.md#domaininfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**disable**](domain.md#disable) </div> | <div style="width:200px; text-align:center;">    [DomainRequest](domain.md#domainrequest)  </div> | <div style="width:200px; text-align:center;">   [DomainInfo](domain.md#domaininfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](domain.md#get) </div> | <div style="width:200px; text-align:center;">    [GetDomainRequest](domain.md#getdomainrequest)  </div> | <div style="width:200px; text-align:center;">   [DomainInfo](domain.md#domaininfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](domain.md#list) </div> | <div style="width:200px; text-align:center;">    [DomainQuery](domain.md#domainquery)  </div> | <div style="width:200px; text-align:center;">   [DomainsInfo](domain.md#domainsinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](domain.md#stat) </div> | <div style="width:200px; text-align:center;">    [DomainStatQuery](domain.md#domainstatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get_public_key**](domain.md#get_public_key) </div> | <div style="width:200px; text-align:center;">  .spaceone.api.core.v1.AuthenticationRequest </div> | <div style="width:200px; text-align:center;">  .spaceone.api.core.v1.AuthenticationResponse </div> | <div style="width:400px;">  </div> | 
 

 
### create
> **POST** /identity/v1/domains
>


| Type | Message |
| :--- | :--- |
| Request | [CreateDomainRequest](domain.md#createdomainrequest) |
| Response |  [DomainInfo](domain.md#domaininfo)  |
 
 

 
### update
> **PUT** /identity/v1/domain/{domain_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateDomainRequest](domain.md#updatedomainrequest) |
| Response |  [DomainInfo](domain.md#domaininfo)  |
 
 

 
### change_auth_plugin
> **PUT** /identity/v1/domain/{domain_id}/change_auth_plugin
>


| Type | Message |
| :--- | :--- |
| Request | [ChangeAuthRequest](domain.md#changeauthrequest) |
| Response |  [DomainInfo](domain.md#domaininfo)  |
 
 

 
### update_plugin
> **PUT** /identity/v1/domain/{domain_id}/plugin
>


| Type | Message |
| :--- | :--- |
| Request | [UpdatePluginRequest](domain.md#updatepluginrequest) |
| Response |  [DomainInfo](domain.md#domaininfo)  |
 
 

 
### verify_plugin
> **POST** /identity/v1/domain/{domain_id}/plugin/verify
>


| Type | Message |
| :--- | :--- |
| Request | [DomainRequest](domain.md#domainrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### delete
> **DELETE** /identity/v1/domain/{domain_id}
>


| Type | Message |
| :--- | :--- |
| Request | [DomainRequest](domain.md#domainrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### enable
> **PUT** /identity/v1/domain/{domain_id}
>


| Type | Message |
| :--- | :--- |
| Request | [DomainRequest](domain.md#domainrequest) |
| Response |  [DomainInfo](domain.md#domaininfo)  |
 
 

 
### disable
> **PUT** /identity/v1/domain/{domain_id}
>


| Type | Message |
| :--- | :--- |
| Request | [DomainRequest](domain.md#domainrequest) |
| Response |  [DomainInfo](domain.md#domaininfo)  |
 
 

 
### get
> **GET** /identity/v1/domain/{domain_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetDomainRequest](domain.md#getdomainrequest) |
| Response |  [DomainInfo](domain.md#domaininfo)  |
 
 

 
### list
> **GET** /identity/v1/domains
>
> **POST** /identity/v1/domains/search



| Type | Message |
| :--- | :--- |
| Request | [DomainQuery](domain.md#domainquery) |
| Response |  [DomainsInfo](domain.md#domainsinfo)  |
 
 

 
### stat
> **POST** /identity/v1/domains/stat
>


| Type | Message |
| :--- | :--- |
| Request | [DomainStatQuery](domain.md#domainstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |
 
 

 
### get_public_key


| Type | Message |
| :--- | :--- |
| Request | [AuthenticationRequest] |
| Response | .spaceone.api.core.v1.AuthenticationResponse |


## 

## Message

### ChangeAuthRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_id |string|✅| |
| plugin_info |[PluginInfo](domain.md#plugininfo)|❌| |
| release_auth_plugin |bool|❌| |

### CreateDomainRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| plugin_info |[PluginInfo](domain.md#plugininfo)|❌| |
| config |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### DomainInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">plugin_info</td>
      <td style="text-align:left"><a href="domain.md#plugininfo">PluginInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">config</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">deleted_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### DomainQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### DomainRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_id |string|✅| |

### DomainStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |

### DomainsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of DomainInfo](domain.md#domaininfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetDomainRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_id |string|✅| |
| only |list of string|❌| |

### PluginInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">secret_data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">schema</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">metadata</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">upgrade_mode</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>MANUAL</li>
          	<li>AUTO</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### UpdateDomainRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_id |string|✅| |
| plugin_info |[PluginInfo](domain.md#plugininfo)|❌| |
| config |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### UpdatePluginRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">upgrade_mode</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>MANUAL</li>
          	<li>AUTO</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>


