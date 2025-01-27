import asyncio
import os
from datetime import datetime

from tapo import ApiClient
from tapo.requests import EnergyDataInterval

os.environ.setdefault('TAPO_USERNAME', 'hmohammadali2013@gmail.com')
os.environ.setdefault('TAPO_PASSWORD', 'Akljsdkv834183')
os.environ.setdefault('TAPO_IP_ADDRESS', '192.168.1.50')


class TapoDeviceManager:
    def __init__(self):
        # Read credentials from environment variables if not provided
        self.tapo_username = os.getenv('TAPO_USERNAME')
        self.tapo_password = os.getenv('TAPO_PASSWORD')
        self.ip_address = os.getenv('TAPO_IP_ADDRESS')
        self.connected = False
        if not self.tapo_username or not self.tapo_password or not self.ip_address:
            raise ValueError("TAPO_USERNAME, TAPO_PASSWORD, and TAPO_IP_ADDRESS must be set either as arguments or environment variables.")

        self.client = ApiClient(self.tapo_username, self.tapo_password)
        self.device = None

    async def connect(self):
        # Initialize the device object
        self.device = await self.client.p110(self.ip_address)
        self.connected = True

    async def turn_on(self):
        if self.device:
            await self.device.on()
        else:
            raise Exception("Device not connected. Call 'connect()' first.")

    async def turn_off(self):
        if self.device:
            await self.device.off()
        else:
            raise Exception("Device not connected. Call 'connect()' first.")

    async def get_device_info(self):
        if self.device:
            device_info = await self.device.get_device_info()
            return device_info.to_dict()
        else:
            raise Exception("Device not connected. Call 'connect()' first.")

    async def get_device_usage(self):
        if self.device:
            device_usage = await self.device.get_device_usage()
            return device_usage.to_dict()
        else:
            raise Exception("Device not connected. Call 'connect()' first.")

    async def get_current_power(self):
        if self.device:
            current_power = await self.device.get_current_power()
            return current_power.to_dict()
        else:
            raise Exception("Device not connected. Call 'connect()' first.")

    async def get_energy_usage(self):
        if self.device:
            energy_usage = await self.device.get_energy_usage()
            return energy_usage.to_dict()
        else:
            raise Exception("Device not connected. Call 'connect()' first.")

    async def get_energy_data_hourly(self, date=None):
        if self.device:
            date = date or datetime.today()
            energy_data_hourly = await self.device.get_energy_data(
                EnergyDataInterval.Hourly, date
            )
            return energy_data_hourly.to_dict()
        else:
            raise Exception("Device not connected. Call 'connect()' first.")

    async def get_energy_data_daily(self, date=None):
        if self.device:
            date = date or datetime.today()
            quarter_start_month = self.get_quarter_start_month(date)
            start_date = datetime(date.year, quarter_start_month, 1)
            energy_data_daily = await self.device.get_energy_data(
                EnergyDataInterval.Daily,
                start_date,
            )
            return energy_data_daily.to_dict()
        else:
            raise Exception("Device not connected. Call 'connect()' first.")

    async def get_energy_data_monthly(self, date=None):
        if self.device:
            date = date or datetime.today()
            start_date = datetime(date.year, 1, 1)
            energy_data_monthly = await self.device.get_energy_data(
                EnergyDataInterval.Monthly,
                start_date,
            )
            return energy_data_monthly.to_dict()
        else:
            raise Exception("Device not connected. Call 'connect()' first.")

    @staticmethod
    def get_quarter_start_month(date: datetime) -> int:
        return 3 * ((date.month - 1) // 3) + 1
