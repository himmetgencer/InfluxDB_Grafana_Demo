# Demonstration of InfluxDB and Grafana

Docker run commands:
```sh
$ docker pull influxdb
$ docker pull telegraf
$ docker pull grafana/grafana
$ docker pull eclipse-mosquitto
```

```sh
$ docker run -i -t --name=influxdb -v C:\Users\Exception\Desktop\git\InfluxDB_Grafana_Demo\conf\influxdb\influxdb.conf:/etc/influxdb/influxdb.conf -p 8086:8086 influxdb
```

```sh
$ docker run -i -t --name=telegraf -v C:\Users\Exception\Desktop\git\InfluxDB_Grafana_Demo\conf\telegraf\telegraf.conf:/etc/telegraf/telegraf.conf --network="host" telegraf
```

```sh
$ docker run -i -t --name=mqtt -v C:\Users\Exception\Desktop\git\InfluxDB_Grafana_Demo\conf\mqtt\mosquitto.conf:/mosquitto/config/mosquitto.conf --user 0 -p 1883:1883 -p 9001:9001 eclipse-mosquitto
```

```sh
$ docker run -i -t --name=grafana --user 0 -p 3000:3000 --link influxdb grafana/grafana
```

Debugging in InfluxDB Container:
```sh
$ docker exec -i -t influxdb influx
$ show databases
$ use db_name
$ show measurements
```

Debugging in InfluxDB Container:
```sh
$ mosquitto_sub -v -h localhost -t '#'
```

go to bash mqtt container's shell script:
```sh
$ docker exec -i -t mqtt "bin/sh"
```

| Description | Link |
| ------ | ------ |
| telegraf json | https://github.com/influxdata/telegraf/tree/master/plugins/parsers/json |

### Todos
- Create docker-compose.yml
