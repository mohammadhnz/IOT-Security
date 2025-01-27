import asyncio
from time import sleep

from device.handlers.tapo_client.m110 import TapoDeviceManager


async def main():
    device_manager = TapoDeviceManager()
    await device_manager.connect()

    await device_manager.turn_off()
    sleep(1)
    await device_manager.turn_on()

    # Retrieve device information
    device_info = await device_manager.get_device_info()
    print(f"Device info: {device_info}")

    # Retrieve device usage
    device_usage = await device_manager.get_device_usage()
    print(f"Device usage: {device_usage}")

    # Retrieve current power
    current_power = await device_manager.get_current_power()
    print(f"Current power: {current_power}")

    # Retrieve energy usage
    energy_usage = await device_manager.get_energy_usage()
    print(f"Energy usage: {energy_usage}")

    # Retrieve energy data (hourly)
    energy_data_hourly = await device_manager.get_energy_data_hourly()
    print(f"Energy data (hourly): {energy_data_hourly}")

    # Retrieve energy data (daily)
    energy_data_daily = await device_manager.get_energy_data_daily()
    print(f"Energy data (daily): {energy_data_daily}")

    # Retrieve energy data (monthly)
    energy_data_monthly = await device_manager.get_energy_data_monthly()
    print(f"Energy data (monthly): {energy_data_monthly}")

    # Close the device manager when done
if __name__ == "__main__":
    asyncio.run(main())