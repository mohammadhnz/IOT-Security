# System Setup and Configuration

## 1. Overview
This guide helps you start all containers via Docker Compose, confirm Mosquitto (MQTT) is running, configure the hub, and test event forwarding between the hub and proxy.  
Example network IP: `192.168.1.53`.

---

## 2. Prerequisites
- Docker and Docker Compose installed.  
- MQTT Explorer (or another MQTT monitoring tool) — optional but recommended.  
- Local network IP address (e.g., `192.168.1.53`) for hosting.

---

## 3. Start the System Pods
1. In your project directory, run:
   ```bash
   docker-compose up -d
   ```
2. Verify that the containers are running:
   ```bash
   docker ps
   ```

---

## 4. Confirm Mosquitto (MQTT) is Running
1. Mosquitto should be running on port **1883**.  
2. Credentials:  
   - Username: `mqtt_user`  
   - Password: `12345`  
3. (Optional) Connect via MQTT Explorer:  
   - Host (For example): `192.168.1.53`  
   - Port: `1883`  
   - Username: `mqtt_user`  
   - Password: `12345`

---

## 5. Configure the Hub
1. In the **MQTT Device Creator** on the hub, set:
   - Broker IP (For example): `192.168.1.53`  
   - Port: `1883`  
   - Username: `mqtt_user`  
   - Password: `12345`  
2. Confirm other required parameters remain as previously configured.

---

## 6. Test Hub–Proxy Connection
1. Generate “noise” (test data or events) on the hub based on your predefined rules.  
2. Check the proxy logs to confirm that these events are captured.  
3. If the fired events appear in the proxy, your system is connected correctly.
