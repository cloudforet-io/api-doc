---
title: "Protocol"
linkTitle: "Protocol"
weight: 3
bookFlatSection: true
---
# [Protocol](#Protocol)
A Protocol defines the method to use when dispatching Notifications via a channel.


>  **Package : spaceone.api.notification.v1**

<br>
<br>

## Protocol





**Protocol Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Protocol#create) | [CreateProtocolRequest](Protocol#createprotocolrequest) | [ProtocolInfo](./Protocol#protocolinfo) |
| [**update**](./Protocol#update) | [UpdateProtocolRequest](Protocol#updateprotocolrequest) | [ProtocolInfo](./Protocol#protocolinfo) |
| [**update_plugin**](./Protocol#update_plugin) | [UpdateProtocolPluginRequest](Protocol#updateprotocolpluginrequest) | [ProtocolInfo](./Protocol#protocolinfo) |
| [**enable**](./Protocol#enable) | [ProtocolRequest](Protocol#protocolrequest) | [ProtocolInfo](./Protocol#protocolinfo) |
| [**disable**](./Protocol#disable) | [ProtocolRequest](Protocol#protocolrequest) | [ProtocolInfo](./Protocol#protocolinfo) |
| [**delete**](./Protocol#delete) | [ProtocolRequest](Protocol#protocolrequest) | [Empty](./Protocol#empty) |
| [**get**](./Protocol#get) | [GetProtocolRequest](Protocol#getprotocolrequest) | [ProtocolInfo](./Protocol#protocolinfo) |
| [**list**](./Protocol#list) | [ProtocolQuery](Protocol#protocolquery) | [ProtocolsInfo](./Protocol#protocolsinfo) |
| [**stat**](./Protocol#stat) | [ProtocolStatQuery](Protocol#protocolstatquery) | [Struct](./Protocol#struct) |



    
<br>

### create

Creates a new Protocol. When creating a protocol, you must specify the plugins provided from the repository, and you must also set the credentials to be set in the plugin if necessary.



> **POST** /notification/v1/protocol/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateProtocolRequest](./Protocol#createprotocolrequest)

* **name** (string)  `Required` 

  *The name of Protocol. It can have a maximum of 255 characters.*


* **plugin_info** (PluginRequest)  `Required` 

  *Describe a Plugin information for protocol that include was used plugin, specific version, schema etc.*


* **domain_id** (string)  `Required` 

  *The ID of domain to which the Protocol belongs.*


* **tags** (Struct) 

  *The tags for protocol.*





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProtocolInfo](#PROTOCOLINFO)
* **protocol_id** (string)  `Required` 

  The ID of Protocol.

* **name** (string)  `Required` 

  The name of Protocol.

* **state** (ProtocolState)  `Required` 

  The state of Protocol.
ENABLED or DISABLED only.

* **protocol_type** (ProtocolType)  `Required` 

  desc : The type of Protocol.
INTERNAL or EXTERNAL only.

* **resource_type** (string)  `Required` 

  desc : Resource type for Protocol. Currently only identity.Project or identity.User can be set.

* **capability** (Struct)  `Required` 

  desc : The capability information for the Protocol. It included supported schema for the Protocol.

* **plugin_info** (PluginInfo)  `Required` 

  the plugin information set in Protocol.

* **tags** (Struct)  `Required` 

  The tags for protocol.

* **domain_id** (string)  `Required` 

  The ID of domain to which the Protocol belongs.

* **created_at** (string)  `Required` 

  Protocol creation time.



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific Protocol. The method `update` can update the name and tags only. If you want to update the plugin version or options, you can use `update_plugin` method.



> **POST** /notification/v1/protocol/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateProtocolRequest](./Protocol#updateprotocolrequest)

* **protocol_id** (string)  `Required` 

  *The ID of Protocol.*


* **domain_id** (string)  `Required` 

  *The ID of domain to which the Protocol belongs.*


* **name** (string) 

  *The Name of Protocol. It can have a maximum of 255 characters.*


* **tags** (Struct) 

  *The tags for protocol. When updating, existing tag information is deleted all and will be updated with new.*





{{< highlight json >}}
{
   "protocol_id": "protocol-123456789012",
   "name": "Email-test",
   "tags": {
       "type": "test"
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProtocolInfo](#PROTOCOLINFO)
* **protocol_id** (string)  `Required` 

  The ID of Protocol.

* **name** (string)  `Required` 

  The name of Protocol.

* **state** (ProtocolState)  `Required` 

  The state of Protocol.
ENABLED or DISABLED only.

* **protocol_type** (ProtocolType)  `Required` 

  desc : The type of Protocol.
INTERNAL or EXTERNAL only.

* **resource_type** (string)  `Required` 

  desc : Resource type for Protocol. Currently only identity.Project or identity.User can be set.

* **capability** (Struct)  `Required` 

  desc : The capability information for the Protocol. It included supported schema for the Protocol.

* **plugin_info** (PluginInfo)  `Required` 

  the plugin information set in Protocol.

* **tags** (Struct)  `Required` 

  The tags for protocol.

* **domain_id** (string)  `Required` 

  The ID of domain to which the Protocol belongs.

* **created_at** (string)  `Required` 

  Protocol creation time.



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update_plugin

Updates a plugin for a Protocol. It is usually used when redeploying a plugin to a new version.



> **POST** /notification/v1/protocol/update-plugin
>





 {{< tabs " update_plugin " >}}

 {{< tab "Request Example" >}}



[UpdateProtocolPluginRequest](./Protocol#updateprotocolpluginrequest)

* **protocol_id** (string)  `Required` 

  *The ID of Protocol.*


* **domain_id** (string)  `Required` 

  *The ID of domain to which the Protocol belongs.*


* **version** (string) 

  *The version of plugin you want to update. Version means the tags of plugin container image in repository that specific market place.*


* **options** (Struct) 

  *The Options that contains information about using plugin.*





{{< highlight json >}}
{
   "protocol_id": "protocol-123456789012",
   "version": "1.0.2",
   "options": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProtocolInfo](#PROTOCOLINFO)
* **protocol_id** (string)  `Required` 

  The ID of Protocol.

* **name** (string)  `Required` 

  The name of Protocol.

* **state** (ProtocolState)  `Required` 

  The state of Protocol.
ENABLED or DISABLED only.

* **protocol_type** (ProtocolType)  `Required` 

  desc : The type of Protocol.
INTERNAL or EXTERNAL only.

* **resource_type** (string)  `Required` 

  desc : Resource type for Protocol. Currently only identity.Project or identity.User can be set.

* **capability** (Struct)  `Required` 

  desc : The capability information for the Protocol. It included supported schema for the Protocol.

* **plugin_info** (PluginInfo)  `Required` 

  the plugin information set in Protocol.

* **tags** (Struct)  `Required` 

  The tags for protocol.

* **domain_id** (string)  `Required` 

  The ID of domain to which the Protocol belongs.

* **created_at** (string)  `Required` 

  Protocol creation time.



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### enable

Enables a specific Protocol. If the Protocol is enabled, the Protocol can be used and the Notification can be dispatched.



> **POST** /notification/v1/protocol/enable
>





 {{< tabs " enable " >}}

 {{< tab "Request Example" >}}



[ProtocolRequest](./Protocol#protocolrequest)

* **protocol_id** (string)  `Required` 

  *The ID of Protocol.*


* **domain_id** (string)  `Required` 

  *The ID of domain to which the Protocol belongs.*





{{< highlight json >}}
{
   "protocol_id": "protocol-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProtocolInfo](#PROTOCOLINFO)
* **protocol_id** (string)  `Required` 

  The ID of Protocol.

* **name** (string)  `Required` 

  The name of Protocol.

* **state** (ProtocolState)  `Required` 

  The state of Protocol.
ENABLED or DISABLED only.

* **protocol_type** (ProtocolType)  `Required` 

  desc : The type of Protocol.
INTERNAL or EXTERNAL only.

* **resource_type** (string)  `Required` 

  desc : Resource type for Protocol. Currently only identity.Project or identity.User can be set.

* **capability** (Struct)  `Required` 

  desc : The capability information for the Protocol. It included supported schema for the Protocol.

* **plugin_info** (PluginInfo)  `Required` 

  the plugin information set in Protocol.

* **tags** (Struct)  `Required` 

  The tags for protocol.

* **domain_id** (string)  `Required` 

  The ID of domain to which the Protocol belongs.

* **created_at** (string)  `Required` 

  Protocol creation time.



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### disable

Disables a specific Protocol. If a Protocol is disabled, the Notification will not be dispatched, even if it is created.



> **POST** /notification/v1/protocol/disable
>





 {{< tabs " disable " >}}

 {{< tab "Request Example" >}}



[ProtocolRequest](./Protocol#protocolrequest)

* **protocol_id** (string)  `Required` 

  *The ID of Protocol.*


* **domain_id** (string)  `Required` 

  *The ID of domain to which the Protocol belongs.*





{{< highlight json >}}
{
   "protocol_id": "protocol-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProtocolInfo](#PROTOCOLINFO)
* **protocol_id** (string)  `Required` 

  The ID of Protocol.

* **name** (string)  `Required` 

  The name of Protocol.

* **state** (ProtocolState)  `Required` 

  The state of Protocol.
ENABLED or DISABLED only.

* **protocol_type** (ProtocolType)  `Required` 

  desc : The type of Protocol.
INTERNAL or EXTERNAL only.

* **resource_type** (string)  `Required` 

  desc : Resource type for Protocol. Currently only identity.Project or identity.User can be set.

* **capability** (Struct)  `Required` 

  desc : The capability information for the Protocol. It included supported schema for the Protocol.

* **plugin_info** (PluginInfo)  `Required` 

  the plugin information set in Protocol.

* **tags** (Struct)  `Required` 

  The tags for protocol.

* **domain_id** (string)  `Required` 

  The ID of domain to which the Protocol belongs.

* **created_at** (string)  `Required` 

  Protocol creation time.



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific Protocol. If there exists a channel using the Protocol, it cannot be deleted.



> **POST** /notification/v1/protocol/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[ProtocolRequest](./Protocol#protocolrequest)

* **protocol_id** (string)  `Required` 

  *The ID of Protocol.*


* **domain_id** (string)  `Required` 

  *The ID of domain to which the Protocol belongs.*





{{< highlight json >}}
{
   "protocol_id": "protocol-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Protocol. Prints detailed information about the Protocol.



> **POST** /notification/v1/protocol/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetProtocolRequest](./Protocol#getprotocolrequest)

* **protocol_id** (string)  `Required` 

  *The ID of Protocol.*


* **domain_id** (string)  `Required` 

  *The ID of domain to which the Protocol belongs.*


* **only** (string) 

  *The list of the Protocol information column you want to be returned. It must be specified in the ProtocolInfo.*





{{< highlight json >}}
{
   "protocol_id": "protocol-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProtocolInfo](#PROTOCOLINFO)
* **protocol_id** (string)  `Required` 

  The ID of Protocol.

* **name** (string)  `Required` 

  The name of Protocol.

* **state** (ProtocolState)  `Required` 

  The state of Protocol.
ENABLED or DISABLED only.

* **protocol_type** (ProtocolType)  `Required` 

  desc : The type of Protocol.
INTERNAL or EXTERNAL only.

* **resource_type** (string)  `Required` 

  desc : Resource type for Protocol. Currently only identity.Project or identity.User can be set.

* **capability** (Struct)  `Required` 

  desc : The capability information for the Protocol. It included supported schema for the Protocol.

* **plugin_info** (PluginInfo)  `Required` 

  the plugin information set in Protocol.

* **tags** (Struct)  `Required` 

  The tags for protocol.

* **domain_id** (string)  `Required` 

  The ID of domain to which the Protocol belongs.

* **created_at** (string)  `Required` 

  Protocol creation time.



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of Protocols. You can use a query to get a filtered list of Protocols.



> **POST** /notification/v1/protocol/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[ProtocolQuery](./Protocol#protocolquery)

* **domain_id** (string)  `Required` 

  *The ID of domain to which the Protocol belongs.*


* **query** (Query) 

  *Query format provided by SpaceONE. Please check the link for more information.*


* **protocol_id** (string) 

  *The ID of Protocol.*


* **name** (string) 

  *The name of Protocol.*


* **state** (ProtocolState) 

  *The state of Protocol. ENABLED or DISABLED only.*


* **protocol_type** (ProtocolType) 

  *The type of Protocol. INTERNAL or EXTERNAL only.*





{{< highlight json >}}
{
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProtocolsInfo](#PROTOCOLSINFO)
* **results** (ProtocolInfo)  `Required` 

  List of queried protocols.

* **total_count** (int32)  `Required` 

  Total counts of queried Protocols.



{{< highlight json >}}
{
      "results":[
         {
            "protocol_id":"protocol-123456789012",
            "name":"Email",
            "state":"ENABLED",
            "protocol_type":"EXTERNAL",
            "capability":{
               "supported_schema":[
                  "email_smtp"
               ]
            },
            "plugin_info":{
               "plugin_id":"plugin-email-noti-protocol",
               "version":"1.0.1",
               "options":{

               },
               "secret_id":"secret-123456789012",
               "metadata":{
                  "data_type":"PLAIN_TEXT",
                  "data":{
                     "schema":{
                        "properties":{
                           "email":{
                              "pattern":"^[\\W]*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4}[\\W]*,{1}[\\W]*)*([\\w+\\-.%]+@[\\w\\-.]+\\.[A-Za-z]{2,4})[\\W]*$",
                              "examples":[
                                 "user1@test.com, user2@test.com"
                              ],
                              "minLength":10.0,
                              "description":"Email address to receive notifications",
                              "type":"string",
                              "title":"Email Address"
                           }
                        },
                        "required":[
                           "email"
                        ],
                        "type":"object"
                     }
                  }
               },
               "upgrade_mode":"AUTO"
            },
            "tags":{

            },
            "domain_id":"domain-123456789012",
            "created_at":"2022-01-01T07:55:57.043Z"
         }
      ],
      "total_count":1
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /notification/v1/protocol/stat
>






    


<br>
<br>

## Message



### CreateProtocolRequest
* **name** (string)  `Required` 

  *The name of Protocol. It can have a maximum of 255 characters.*

    
* **plugin_info** (PluginRequest)  `Required` 

  *Describe a Plugin information for protocol that include was used plugin, specific version, schema etc.*

    
* **domain_id** (string)  `Required` 

  *The ID of domain to which the Protocol belongs.*

    
* **tags** (Struct) 

  *The tags for protocol.*

    <br>

### GetProtocolRequest
* **protocol_id** (string)  `Required` 

  *The ID of Protocol.*

    
* **domain_id** (string)  `Required` 

  *The ID of domain to which the Protocol belongs.*

    
* **only** (string) 

  *The list of the Protocol information column you want to be returned. It must be specified in the ProtocolInfo.*

    <br>

### PluginInfo
* **plugin_id** (string)  `Required` 

  *The ID of plugin set in the Protocol.*

    
* **version** (string)  `Required` 

  *The version of plugin.*

    
* **options** (Struct)  `Required` 

  *The Options that contains information about using plugin.*

    
* **secret_id** (string)  `Required` 

  *The ID of the Secret containing encrypted data to be used in the plugin.*

    
* **metadata** (Struct)  `Required` 

  *The metadata of plugin. It includes schema for the data that must be set for the Channel when creating the Channel using a Protocol.
The schema follows the JSON Schema format.*

    
* **upgrade_mode** (UpgradeMode)  `Required` 

  *Auto upgrade for plugin.
If the upgrade_mode is AUTO, check the latest plugin version when running the plugin, and if a new version is existed, replace the plugin and then run it.*

    <br>

### PluginRequest
* **plugin_id** (string)  `Required` 

  *The ID of plugin.*

    
* **version** (string)  `Required` 

  *The version of plugin.*

    
* **options** (Struct) 

  *The Options that contains information about using plugin.*

    
* **secret_data** (Struct) 

  *The data for using plugin if necessary. This data is encrypted and stored in the Secret service.*

    
* **schema** (string) 

  *The name of schema.
When the secret_data is stored in the Secret service, it can be set with schema if the schema is existed.
The schema is provided through the Repository service.*

    
* **upgrade_mode** (UpgradeMode) 

  *Auto upgrade feature for plugin.
If the upgrade mode is AUTO, check the latest plugin version when running the plugin, and if a new version is existed, replace the plugin and then run it.*

    <br>

### ProtocolInfo
* **protocol_id** (string)  `Required` 

  *The ID of Protocol.*

    
* **name** (string)  `Required` 

  *The name of Protocol.*

    
* **state** (ProtocolState)  `Required` 

  *The state of Protocol.
ENABLED or DISABLED only.*

    
* **protocol_type** (ProtocolType)  `Required` 

  *desc : The type of Protocol.
INTERNAL or EXTERNAL only.*

    
* **resource_type** (string)  `Required` 

  *desc : Resource type for Protocol. Currently only identity.Project or identity.User can be set.*

    
* **capability** (Struct)  `Required` 

  *desc : The capability information for the Protocol. It included supported schema for the Protocol.*

    
* **plugin_info** (PluginInfo)  `Required` 

  *the plugin information set in Protocol.*

    
* **tags** (Struct)  `Required` 

  *The tags for protocol.*

    
* **domain_id** (string)  `Required` 

  *The ID of domain to which the Protocol belongs.*

    
* **created_at** (string)  `Required` 

  *Protocol creation time.*

    <br>

### ProtocolQuery
* **domain_id** (string)  `Required` 

  *The ID of domain to which the Protocol belongs.*

    
* **query** (Query) 

  *Query format provided by SpaceONE. Please check the link for more information.*

    
* **protocol_id** (string) 

  *The ID of Protocol.*

    
* **name** (string) 

  *The name of Protocol.*

    
* **state** (ProtocolState) 

  *The state of Protocol. ENABLED or DISABLED only.*

    
* **protocol_type** (ProtocolType) 

  *The type of Protocol. INTERNAL or EXTERNAL only.*

    <br>

### ProtocolRequest
* **protocol_id** (string)  `Required` 

  *The ID of Protocol.*

    
* **domain_id** (string)  `Required` 

  *The ID of domain to which the Protocol belongs.*

    <br>

### ProtocolStatQuery
* **query** (StatisticsQuery)  `Required` 

  *Statistics Query format provided by SpaceONE. Please check the link for more information.*

    
* **domain_id** (string)  `Required` 

  *The ID of domain to which the Protocol belongs.*

    <br>

### ProtocolsInfo
* **results** (ProtocolInfo)  `Required` 

  *List of queried protocols.*

    
* **total_count** (int32)  `Required` 

  *Total counts of queried Protocols.*

    <br>

### UpdateProtocolPluginRequest
* **protocol_id** (string)  `Required` 

  *The ID of Protocol.*

    
* **domain_id** (string)  `Required` 

  *The ID of domain to which the Protocol belongs.*

    
* **version** (string) 

  *The version of plugin you want to update. Version means the tags of plugin container image in repository that specific market place.*

    
* **options** (Struct) 

  *The Options that contains information about using plugin.*

    <br>

### UpdateProtocolRequest
* **protocol_id** (string)  `Required` 

  *The ID of Protocol.*

    
* **domain_id** (string)  `Required` 

  *The ID of domain to which the Protocol belongs.*

    
* **name** (string) 

  *The Name of Protocol. It can have a maximum of 255 characters.*

    
* **tags** (Struct) 

  *The tags for protocol. When updating, existing tag information is deleted all and will be updated with new.*

    <br>
