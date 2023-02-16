---
description: A Protocol defines the method to use when dispatching Notifications via a channel.
---
# Protocol

>  **Package : spaceone.api.notification.v1**

## Protocol

{% hint style="info" %}
**Protocol Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](protocol.md#create)|   [CreateProtocolRequest](protocol.md#createprotocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) |
| [**update**](protocol.md#update)|   [UpdateProtocolRequest](protocol.md#updateprotocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) |
| [**update_plugin**](protocol.md#update_plugin)|   [UpdateProtocolPluginRequest](protocol.md#updateprotocolpluginrequest) |   [ProtocolInfo](protocol.md#protocolinfo) |
| [**enable**](protocol.md#enable)|   [ProtocolRequest](protocol.md#protocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) |
| [**disable**](protocol.md#disable)|   [ProtocolRequest](protocol.md#protocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) |
| [**delete**](protocol.md#delete)|   [ProtocolRequest](protocol.md#protocolrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](protocol.md#get)|   [GetProtocolRequest](protocol.md#getprotocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) |
| [**list**](protocol.md#list)|   [ProtocolQuery](protocol.md#protocolquery) |   [ProtocolsInfo](protocol.md#protocolsinfo) |
| [**stat**](protocol.md#stat)|   [ProtocolStatQuery](protocol.md#protocolstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** notification/v1/protocol/create
>

> Creates a new Protocol. When creating a protocol, you must specify the plugins provided from the repository, and you must also set the credentials to be set in the plugin if necessary.

| Type | Message |
| :--- | :--- |
| Request | [CreateProtocolRequest](protocol.md#createprotocolrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "Email",
    "plugin_info": {
        "plugin_id": "plugin-email-noti-protocol",
        "version": "1.0.1",
        "options": {},
        "secret_id": "secret-123546789012",
        "metadata": {
            "data": {
                "schema": {
                    "properties": {
                        "email": {
                            "pattern": "^[\\W]*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4}[\\W]*,{1}[\\W]*)*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4})[\\W]*$",
                            "examples": [
                                "user1@test.com, user2@test.com"
                            ],
                            "minLength": 10.0,
                            "description": "Email address to receive notifications",
                            "type": "string",
                            "title": "Email Address"
                        }
                    },
                    "required": [
                        "email"
                    ],
                    "type": "object"
                }
            },
            "data_type": "PLAIN_TEXT"
        },
        "upgrade_mode": "AUTO"
    },
    "tags": {}
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "protocol_id": "protocol-123546789012",
    "name": "Email",
    "state": "ENABLED",
    "protocol_type": "EXTERNAL",
    "capability": {
        "supported_schema": [
            "email_smtp"
        ]
    },
    "plugin_info": {
        "plugin_id": "plugin-email-noti-protocol",
        "version": "1.0.1",
        "options": {},
        "secret_id": "secret-123546789012",
        "metadata": {
            "data": {
                "schema": {
                    "properties": {
                        "email": {
                            "pattern": "^[\\W]*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4}[\\W]*,{1}[\\W]*)*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4})[\\W]*$",
                            "examples": [
                                "user1@test.com, user2@test.com"
                            ],
                            "minLength": 10.0,
                            "description": "Email address to receive notifications",
                            "type": "string",
                            "title": "Email Address"
                        }
                    },
                    "required": [
                        "email"
                    ],
                    "type": "object"
                }
            },
            "data_type": "PLAIN_TEXT"
        },
        "upgrade_mode": "AUTO"
    },
    "tags": {},
    "domain_id": "domain-123546789012",
    "created_at": "2022-01-01T07:55:57.043Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **POST** notification/v1/protocol/update
>

> Updates a specific Protocol. The method `update` can update the name and tags only. If you want to update the plugin version or options, you can use `update_plugin` method.

| Type | Message |
| :--- | :--- |
| Request | [UpdateProtocolRequest](protocol.md#updateprotocolrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "protocol_id": "protocol-123456789012",
    "name": "Email-test",
    "tags": {
        "type": "test"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "protocol_id": "protocol-123546789012",
    "name": "Email-test",
    "state": "ENABLED",
    "protocol_type": "EXTERNAL",
    "capability": {
        "supported_schema": [
            "email_smtp"
        ]
    },
    "plugin_info": {
        "plugin_id": "plugin-email-noti-protocol",
        "version": "1.0.1",
        "options": {},
        "secret_id": "secret-123546789012",
        "metadata": {
            "data": {
                "schema": {
                    "properties": {
                        "email": {
                            "pattern": "^[\\W]*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4}[\\W]*,{1}[\\W]*)*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4})[\\W]*$",
                            "examples": [
                                "user1@test.com, user2@test.com"
                            ],
                            "minLength": 10.0,
                            "description": "Email address to receive notifications",
                            "type": "string",
                            "title": "Email Address"
                        }
                    },
                    "required": [
                        "email"
                    ],
                    "type": "object"
                }
            },
            "data_type": "PLAIN_TEXT"
        },
        "upgrade_mode": "AUTO"
    },
    "tags": {
        "type": "test"
    },
    "domain_id": "domain-123546789012",
    "created_at": "2022-01-01T07:55:57.043Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update_plugin
> **POST** notification/v1/protocol/update-plugin
>

> Updates a plugin for a Protocol. It is usually used when redeploying a plugin to a new version.

| Type | Message |
| :--- | :--- |
| Request | [UpdateProtocolPluginRequest](protocol.md#updateprotocolpluginrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "protocol_id": "protocol-123456789012",
    "version": "1.0.2",
    "options": {}
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "protocol_id": "protocol-123546789012",
    "name": "Email-test",
    "state": "ENABLED",
    "protocol_type": "EXTERNAL",
    "capability": {
        "supported_schema": [
            "email_smtp"
        ]
    },
    "plugin_info": {
        "plugin_id": "plugin-email-noti-protocol",
        "version": "1.0.2",
        "options": {},
        "secret_id": "secret-123546789012",
        "metadata": {
            "data": {
                "schema": {
                    "properties": {
                        "email": {
                            "pattern": "^[\\W]*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4}[\\W]*,{1}[\\W]*)*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4})[\\W]*$",
                            "examples": [
                                "user1@test.com, user2@test.com"
                            ],
                            "minLength": 10.0,
                            "description": "Email address to receive notifications",
                            "type": "string",
                            "title": "Email Address"
                        }
                    },
                    "required": [
                        "email"
                    ],
                    "type": "object"
                }
            },
            "data_type": "PLAIN_TEXT"
        },
        "upgrade_mode": "AUTO"
    },
    "tags": {
        "type": "test"
    },
    "domain_id": "domain-123546789012",
    "created_at": "2022-01-01T07:55:57.043Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### enable
> **POST** notification/v1/protocol/enable
>

> Enables a specific Protocol. If the Protocol is enabled, the Protocol can be used and the Notification can be dispatched.

| Type | Message |
| :--- | :--- |
| Request | [ProtocolRequest](protocol.md#protocolrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "protocol_id": "protocol-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "protocol_id": "protocol-123546789012",
    "name": "Email-test",
    "state": "ENABLED",
    "protocol_type": "EXTERNAL",
    "capability": {
        "supported_schema": [
            "email_smtp"
        ]
    },
    "plugin_info": {
        "plugin_id": "plugin-email-noti-protocol",
        "version": "1.0.2",
        "options": {},
        "secret_id": "secret-123546789012",
        "metadata": {
            "data": {
                "schema": {
                    "properties": {
                        "email": {
                            "pattern": "^[\\W]*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4}[\\W]*,{1}[\\W]*)*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4})[\\W]*$",
                            "examples": [
                                "user1@test.com, user2@test.com"
                            ],
                            "minLength": 10.0,
                            "description": "Email address to receive notifications",
                            "type": "string",
                            "title": "Email Address"
                        }
                    },
                    "required": [
                        "email"
                    ],
                    "type": "object"
                }
            },
            "data_type": "PLAIN_TEXT"
        },
        "upgrade_mode": "AUTO"
    },
    "tags": {
        "type": "test"
    },
    "domain_id": "domain-123546789012",
    "created_at": "2022-01-01T07:55:57.043Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### disable
> **POST** notification/v1/protocol/disable
>

> Disables a specific Protocol. If a Protocol is disabled, the Notification will not be dispatched, even if it is created.

| Type | Message |
| :--- | :--- |
| Request | [ProtocolRequest](protocol.md#protocolrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "protocol_id": "protocol-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "protocol_id": "protocol-123546789012",
    "name": "Email-test",
    "state": "DISABLED",
    "protocol_type": "EXTERNAL",
    "capability": {
        "supported_schema": [
            "email_smtp"
        ]
    },
    "plugin_info": {
        "plugin_id": "plugin-email-noti-protocol",
        "version": "1.0.2",
        "options": {},
        "secret_id": "secret-123546789012",
        "metadata": {
            "data": {
                "schema": {
                    "properties": {
                        "email": {
                            "pattern": "^[\\W]*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4}[\\W]*,{1}[\\W]*)*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4})[\\W]*$",
                            "examples": [
                                "user1@test.com, user2@test.com"
                            ],
                            "minLength": 10.0,
                            "description": "Email address to receive notifications",
                            "type": "string",
                            "title": "Email Address"
                        }
                    },
                    "required": [
                        "email"
                    ],
                    "type": "object"
                }
            },
            "data_type": "PLAIN_TEXT"
        },
        "upgrade_mode": "AUTO"
    },
    "tags": {
        "type": "test"
    },
    "domain_id": "domain-123546789012",
    "created_at": "2022-01-01T07:55:57.043Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **POST** notification/v1/protocol/delete
>

> Deletes a specific Protocol. If there exists a channel using the Protocol, it cannot be deleted.

| Type | Message |
| :--- | :--- |
| Request | [ProtocolRequest](protocol.md#protocolrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "protocol_id": "protocol-123456789012"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** notification/v1/protocol/get
>

> Gets a specific Protocol. Prints detailed information about the Protocol.

| Type | Message |
| :--- | :--- |
| Request | [GetProtocolRequest](protocol.md#getprotocolrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "protocol_id": "protocol-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "protocol_id": "protocol-123546789012",
    "name": "Email-test",
    "state": "DISABLED",
    "protocol_type": "EXTERNAL",
    "capability": {
        "supported_schema": [
            "email_smtp"
        ]
    },
    "plugin_info": {
        "plugin_id": "plugin-email-noti-protocol",
        "version": "1.0.2",
        "options": {},
        "secret_id": "secret-123546789012",
        "metadata": {
            "data": {
                "schema": {
                    "properties": {
                        "email": {
                            "pattern": "^[\\W]*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4}[\\W]*,{1}[\\W]*)*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4})[\\W]*$",
                            "examples": [
                                "user1@test.com, user2@test.com"
                            ],
                            "minLength": 10.0,
                            "description": "Email address to receive notifications",
                            "type": "string",
                            "title": "Email Address"
                        }
                    },
                    "required": [
                        "email"
                    ],
                    "type": "object"
                }
            },
            "data_type": "PLAIN_TEXT"
        },
        "upgrade_mode": "AUTO"
    },
    "tags": {
        "type": "test"
    },
    "domain_id": "domain-123546789012",
    "created_at": "2022-01-01T07:55:57.043Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** notification/v1/protocol/list
>

> Gets a list of Protocols. You can use a query to get a filtered list of Protocols.

| Type | Message |
| :--- | :--- |
| Request | [ProtocolQuery](protocol.md#protocolquery) |
| Response |  [ProtocolsInfo](protocol.md#protocolsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {}
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "protocol_id": "protocol-123456789012",
            "name": "Email",
            "state": "ENABLED",
            "protocol_type": "EXTERNAL",
            "capability": {
                "supported_schema": [
                    "email_smtp"
                ]
            },
            "plugin_info": {
                "plugin_id": "plugin-email-noti-protocol",
                "version": "1.0.1",
                "options": {},
                "secret_id": "secret-123456789012",
                "metadata": {
                    "data_type": "PLAIN_TEXT",
                    "data": {
                        "schema": {
                            "properties": {
                                "email": {
                                    "pattern": "^[\\W]*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4}[\\W]*,{1}[\\W]*)*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4})[\\W]*$",
                                    "examples": [
                                        "user1@test.com, user2@test.com"
                                    ],
                                    "minLength": 10.0,
                                    "description": "Email address to receive notifications",
                                    "type": "string",
                                    "title": "Email Address"
                                }
                            },
                            "required": [
                                "email"
                            ],
                            "type": "object"
                        }
                    }
                },
                "upgrade_mode": "AUTO"
            },
            "tags": {},
            "domain_id": "domain-123456789012",
            "created_at": "2022-01-01T07:55:57.043Z"
        }
    ],
    "total_count": 1
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** notification/v1/protocol/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ProtocolStatQuery](protocol.md#protocolstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateProtocolRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| The name of Protocol. It can have a maximum of 255 characters.|
| plugin_info |[PluginRequest](protocol.md#pluginrequest)|✔| Describe a Plugin information for protocol that include was used plugin, specific version, schema etc.|
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| The tags for protocol.|
| domain_id |string|✔| The ID of domain to which the Protocol belongs.|

### GetProtocolRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| protocol_id |string|✔| The ID of Protocol.|
| domain_id |string|✔| The ID of domain to which the Protocol belongs.|
| only |list of string|✘| The list of the Protocol information column you want to be returned. It must be specified in the ProtocolInfo.|

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
<td style="text-align:left">The ID of plugin set in the Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The version of plugin.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">The Options that contains information about using plugin.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of the Secret containing encrypted data to be used in the plugin.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">metadata</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">The metadata of plugin. It includes schema for the data that must be set for the Channel when creating the Channel using a Protocol.The schema follows the JSON Schema format.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">upgrade_mode</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>AUTO</li>
          	<li>MANUAL</li>
        </ul></td>
<td style="text-align:left">Auto upgrade for plugin.If the upgrade_mode is AUTO, check the latest plugin version when running the plugin, and if a new version is existed, replace the plugin and then run it.</td>
   </tr>
  </tbody>
</table>



### PluginRequest
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
      <td style="text-align:left; width:100px;">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The ID of plugin.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The version of plugin.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The Options that contains information about using plugin.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The data for using plugin if necessary. This data is encrypted and stored in the Secret service.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">schema</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The name of schema.When the secret_data is stored in the Secret service, it can be set with schema if the schema is existed.The schema is provided through the Repository service.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">upgrade_mode</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>AUTO</li>
          	<li>MANUAL</li>
        </ul></td>
<td style="text-align:center">✔</td>
<td style="text-align:left">Auto upgrade feature for plugin.If the upgrade mode is AUTO, check the latest plugin version when running the plugin, and if a new version is existed, replace the plugin and then run it.</td>
   </tr>
  </tbody>
</table>



### ProtocolInfo
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
      <td style="text-align:left; width:100px;">protocol_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The name of Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left">The state of Protocol.ENABLED or DISABLED only.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">protocol_type</td>
      <td style="text-align:left"><ul>
          	<li>PROTOCOL_TYPE_NONE</li>
          	<li>INTERNAL</li>
          	<li>EXTERNAL</li>
        </ul></td>
<td style="text-align:left">{}</td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">resource_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">Resource type for Protocol. Currently only identity.Project or identity.User can be set.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">capability</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">The capability information for the Protocol. It included supported schema for the Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">plugin_info</td>
      <td style="text-align:left"><a href="protocol.md#plugininfo">PluginInfo</a></td>
<td style="text-align:left">the plugin information set in Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">The tags for protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of domain to which the Protocol belongs.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">Protocol creation time.</td>
   </tr>
  </tbody>
</table>



### ProtocolQuery
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
<td style="text-align:center">✘</td>
<td style="text-align:left">Query format provided by SpaceONE. Please check the link for more information.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">protocol_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The ID of Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The name of Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The state of Protocol. ENABLED or DISABLED only.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">protocol_type</td>
      <td style="text-align:left"><ul>
          	<li>PROTOCOL_TYPE_NONE</li>
          	<li>INTERNAL</li>
          	<li>EXTERNAL</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The type of Protocol. INTERNAL or EXTERNAL only.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The ID of domain to which the Protocol belongs.</td>
   </tr>
  </tbody>
</table>



### ProtocolRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| protocol_id |string|✔| The ID of Protocol.|
| domain_id |string|✔| The ID of domain to which the Protocol belongs.|

### ProtocolStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| Statistics Query format provided by SpaceONE. Please check the link for more information.|
| domain_id |string|✔| The ID of domain to which the Protocol belongs.|

### ProtocolsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ProtocolInfo](protocol.md#protocolinfo) | List of queried protocols.|
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | Total counts of queried Protocols.|

### UpdateProtocolPluginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| protocol_id |string|✔| The ID of Protocol.|
| version |string|✘| The version of plugin you want to update. Version means the tags of plugin container image in repository that specific market place.|
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| The Options that contains information about using plugin.|
| domain_id |string|✔| The ID of domain to which the Protocol belongs.|

### UpdateProtocolRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| protocol_id |string|✔| The ID of Protocol.|
| name |string|✘| The Name of Protocol. It can have a maximum of 255 characters.|
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| The tags for protocol. When updating, existing tag information is deleted all and will be updated with new.|
| domain_id |string|✔| The ID of domain to which the Protocol belongs.|
