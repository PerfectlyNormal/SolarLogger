import goodwe

async def get_runtime_ppv(ip_address):
    inverter = await goodwe.connect(ip_address, timeout=3, retries=10)
    runtime_data = await inverter.read_runtime_data()

    for sensor in inverter.sensors():
        if sensor.id_ == 'ppv' and sensor.id_ in runtime_data:
            return runtime_data[sensor.id_]

