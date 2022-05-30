---
description:  
---
# Plugin

>  **Package : spaceone.api.repository.v1**

## Plugin

{% hint style="info" %}
**Plugin Methods:**

{%  endhint %}


| Method | Request | Response |
| :-----: | :--------: | :--------: |
| [**register**](plugin.md#register)|   [CreatePluginRequest](plugin.md#createpluginrequest) |   [PluginInfo](plugin.md#plugininfo) |
| [**update**](plugin.md#update)|   [UpdatePluginRequest](plugin.md#updatepluginrequest) |   [PluginInfo](plugin.md#plugininfo) |
| [**deregister**](plugin.md#deregister)|   [PluginRequest](plugin.md#pluginrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**enable**](plugin.md#enable)|   [PluginRequest](plugin.md#pluginrequest) |   [PluginInfo](plugin.md#plugininfo) |
| [**disable**](plugin.md#disable)|   [PluginRequest](plugin.md#pluginrequest) |   [PluginInfo](plugin.md#plugininfo) |
| [**get_versions**](plugin.md#get_versions)|   [RepositoryPluginRequest](plugin.md#repositorypluginrequest) |   [VersionsInfo](plugin.md#versionsinfo) |
| [**get**](plugin.md#get)|   [GetRepositoryPluginRequest](plugin.md#getrepositorypluginrequest) |   [PluginInfo](plugin.md#plugininfo) |
| [**list**](plugin.md#list)|   [PluginQuery](plugin.md#pluginquery) |   [PluginsInfo](plugin.md#pluginsinfo) |
| [**stat**](plugin.md#stat)|   [PluginStatQuery](plugin.md#pluginstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### register
> **POST** /repository/v1/plugins
>


| Type | Message |
| :--- | :--- |
| Request | [CreatePluginRequest](plugin.md#createpluginrequest) |
| Response |  [PluginInfo](plugin.md#plugininfo)  |
 
 

 
### update
> **PUT** /repository/v1/plugin/{plugin_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdatePluginRequest](plugin.md#updatepluginrequest) |
| Response |  [PluginInfo](plugin.md#plugininfo)  |
 
 

 
### deregister
> **DELETE** /repository/v1/plugin/{plugin_id}
>


| Type | Message |
| :--- | :--- |
| Request | [PluginRequest](plugin.md#pluginrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### enable
> **PUT** /repository/v1/plugin/{plugin_id}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [PluginRequest](plugin.md#pluginrequest) |
| Response |  [PluginInfo](plugin.md#plugininfo)  |
 
 

 
### disable
> **PUT** /repository/v1/plugin/{plugin_id}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [PluginRequest](plugin.md#pluginrequest) |
| Response |  [PluginInfo](plugin.md#plugininfo)  |
 
 

 
### get_versions
> **GET** /repository/v1/plugins/{plugin_id}/versions
>


| Type | Message |
| :--- | :--- |
| Request | [RepositoryPluginRequest](plugin.md#repositorypluginrequest) |
| Response |  [VersionsInfo](plugin.md#versionsinfo)  |
 
 

 
### get
> **GET** /repository/v1/plugins/{plugin_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetRepositoryPluginRequest](plugin.md#getrepositorypluginrequest) |
| Response |  [PluginInfo](plugin.md#plugininfo)  |
 
 

 
### list
> **GET** /repository/v1/plugins
>
> **POST** /repository/v1/plugins/search



| Type | Message |
| :--- | :--- |
| Request | [PluginQuery](plugin.md#pluginquery) |
| Response |  [PluginsInfo](plugin.md#pluginsinfo)  |
 
 

 
### stat
> **POST** /repository/v1/plugins/stat
>


| Type | Message |
| :--- | :--- |
| Request | [PluginStatQuery](plugin.md#pluginstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreatePluginRequest
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
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">service_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">image</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">registry_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE_REGISTRY_TYPE</li>
          	<li>DOCKER_HUB</li>
          	<li>AWS_PUBLIC_ECR</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">registry_config</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">capability</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">template</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">labels</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### GetRepositoryPluginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| plugin_id |string|✅| |
| domain_id |string|✅| |
| repository_id |string|❌| |
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
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">image</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">registry_url</td>
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
      <td style="text-align:left; width:100px;">service_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">registry_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE_REGISTRY_TYPE</li>
          	<li>DOCKER_HUB</li>
          	<li>AWS_PUBLIC_ECR</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">registry_config</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">capability</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">template</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">labels</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">repository_info</td>
      <td style="text-align:left"><a href="plugin.md#repositoryinfo">RepositoryInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### PluginQuery
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
      <td style="text-align:left; width:100px;">plugin_id</td>
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
    <tr>
      <td style="text-align:left; width:100px;">service_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">repository_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">registry_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE_REGISTRY_TYPE</li>
          	<li>DOCKER_HUB</li>
          	<li>AWS_PUBLIC_ECR</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### PluginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| plugin_id |string|✅| |
| domain_id |string|✅| |

### PluginStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| repository_id |string|✅| |
| domain_id |string|✅| |

### PluginsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of PluginInfo](plugin.md#plugininfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### RepositoryPluginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| plugin_id |string|✅| |
| domain_id |string|✅| |
| repository_id |string|❌| |

### UpdatePluginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| plugin_id |string|✅| |
| name |string|❌| |
| capability |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| template |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### VersionsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| version |list of string | deprecated field|
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| results |list of string | |
