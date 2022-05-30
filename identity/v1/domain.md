---
description:  
---
# Domain

>  **Package : spaceone.api.identity.v1**

## Domain

{% hint style="info" %}
**Domain Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](domain.md#create)|   [CreateDomainRequest](domain.md#createdomainrequest) |   [DomainInfo](domain.md#domaininfo) |
| [**update**](domain.md#update)|   [UpdateDomainRequest](domain.md#updatedomainrequest) |   [DomainInfo](domain.md#domaininfo) |
| [**change_auth_plugin**](domain.md#change_auth_plugin)|   [ChangeAuthRequest](domain.md#changeauthrequest) |   [DomainInfo](domain.md#domaininfo) |
| [**update_plugin**](domain.md#update_plugin)|   [UpdatePluginRequest](domain.md#updatepluginrequest) |   [DomainInfo](domain.md#domaininfo) |
| [**verify_plugin**](domain.md#verify_plugin)|   [DomainRequest](domain.md#domainrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**delete**](domain.md#delete)|   [DomainRequest](domain.md#domainrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**enable**](domain.md#enable)|   [DomainRequest](domain.md#domainrequest) |   [DomainInfo](domain.md#domaininfo) |
| [**disable**](domain.md#disable)|   [DomainRequest](domain.md#domainrequest) |   [DomainInfo](domain.md#domaininfo) |
| [**get**](domain.md#get)|   [GetDomainRequest](domain.md#getdomainrequest) |   [DomainInfo](domain.md#domaininfo) |
| [**list**](domain.md#list)|   [DomainQuery](domain.md#domainquery) |   [DomainsInfo](domain.md#domainsinfo) |
| [**stat**](domain.md#stat)|   [DomainStatQuery](domain.md#domainstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|
| [**get_public_key**](domain.md#get_public_key)| .spaceone.api.core.v1.AuthenticationRequest|  .spaceone.api.core.v1.AuthenticationResponse| 
 

 
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
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">plugin_info</td>
      <td style="text-align:left"><a href="domain.md#plugininfo">PluginInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">config</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">deleted_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### DomainQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
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
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">schema</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">metadata</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">upgrade_mode</td>
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
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">upgrade_mode</td>
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


