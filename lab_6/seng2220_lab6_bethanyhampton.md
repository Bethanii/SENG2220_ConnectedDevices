[
    {
        "id": "785232aa55fca875",
        "type": "tab",
        "label": "Lab 6",
        "disabled": false,
        "info": "",
        "env": []
    },
    {
        "id": "21de31edec6baff4",
        "type": "debug",
        "z": "785232aa55fca875",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "statusVal": "",
        "statusType": "auto",
        "x": 410,
        "y": 140,
        "wires": []
    },
    {
        "id": "29192fe417936b9c",
        "type": "serial in",
        "z": "785232aa55fca875",
        "name": "",
        "serial": "46bb8706ffd0a530",
        "x": 190,
        "y": 140,
        "wires": [
            [
                "21de31edec6baff4"
            ]
        ]
    },
    {
        "id": "2799295fda3d20c6",
        "type": "mqtt in",
        "z": "785232aa55fca875",
        "name": "Subscriber",
        "topic": "hambetn/pyiot",
        "qos": "2",
        "datatype": "auto",
        "broker": "cdd7e2fa877d62d0",
        "nl": false,
        "rap": true,
        "rh": 0,
        "inputs": 0,
        "x": 180,
        "y": 320,
        "wires": [
            [
                "46492dc2c834b2ca"
            ]
        ]
    },
    {
        "id": "763583db86325957",
        "type": "inject",
        "z": "785232aa55fca875",
        "name": "",
        "props": [
            {
                "p": "topic",
                "vt": "str"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "topic": "",
        "x": 150,
        "y": 560,
        "wires": [
            [
                "4c3a50ed28901953"
            ]
        ]
    },
    {
        "id": "46492dc2c834b2ca",
        "type": "debug",
        "z": "785232aa55fca875",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "statusVal": "",
        "statusType": "auto",
        "x": 410,
        "y": 320,
        "wires": []
    },
    {
        "id": "4c3a50ed28901953",
        "type": "mqtt out",
        "z": "785232aa55fca875",
        "name": "Publisher",
        "topic": "hambetn/pyiot",
        "qos": "",
        "retain": "",
        "respTopic": "",
        "contentType": "",
        "userProps": "",
        "correl": "",
        "expiry": "",
        "broker": "cdd7e2fa877d62d0",
        "x": 480,
        "y": 560,
        "wires": []
    },
    {
        "id": "46bb8706ffd0a530",
        "type": "serial-port",
        "serialport": "COM5",
        "serialbaud": "9600",
        "databits": "8",
        "parity": "none",
        "stopbits": "1",
        "waitfor": "",
        "dtr": "none",
        "rts": "none",
        "cts": "none",
        "dsr": "none",
        "newline": "\\n",
        "bin": "false",
        "out": "char",
        "addchar": "",
        "responsetimeout": "10000"
    },
    {
        "id": "cdd7e2fa877d62d0",
        "type": "mqtt-broker",
        "name": "",
        "broker": "10.43.1.103",
        "port": "1883",
        "clientid": "",
        "autoConnect": true,
        "usetls": false,
        "protocolVersion": "4",
        "keepalive": "60",
        "cleansession": true,
        "birthTopic": "",
        "birthQos": "0",
        "birthPayload": "",
        "birthMsg": {},
        "closeTopic": "",
        "closeQos": "0",
        "closePayload": "",
        "closeMsg": {},
        "willTopic": "",
        "willQos": "0",
        "willPayload": "",
        "willMsg": {},
        "sessionExpiry": ""
    }
]