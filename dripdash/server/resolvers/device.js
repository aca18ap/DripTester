const { PrismaClient } = require("@prisma/client");
const prisma = new PrismaClient();

const Device = {
  owner: async (device) => {
    return await prisma.device.findOne({ where: { id: device.id }}).owner();
  },
  location: (device) => {
    if (!device.longitude || !device.latitude) return null;
    return {
      latitude: device.latitude,
      longitude: device.longitude
    }
  },
  data: async (device, { from }) => {
    return await prisma.dataEntry.findMany({
      where: {
        deviceId: device.id,
        timestamp: from ? { gte: new Date(from) } : {}
      }
    })
  },
  latest: async (device) => {
    const latest = await prisma.dataEntry.findMany({
      where: { deviceId: device.id },
      orderBy: { timestamp: "desc" },
      take: 1
    })
    
    return latest.length === 1 ? latest[0] : null;
  },
  status: async (device) => {
    let latest = await prisma.dataEntry.findMany({
      where: { deviceId: device.id },
      orderBy: { timestamp: "desc" },
      take: 1
    });

    latest = latest[0];

    if (!latest) {
      return "KO"
    } else if (Date.now() - new Date(latest.timestamp) > 30000) {
      // Device is offline, therefore unknown.
      return "UNKNOWN";
    } else if (latest.rssi <= -70) {
      // Wi-Fi signal poor, warning.
      return "WARN";
    } else {
      return "OK";
    }
  },
  glances: async (device) => {
    let latest = await prisma.dataEntry.findMany({
      where: { deviceId: device.id },
      orderBy: { timestamp: "desc" },
      take: 1
    });

    latest = latest[0];

    let glances = [];

    if (Date.now() - new Date(latest.timestamp) > 30000) {
      glances.push({
        title: "Connection",
        text: "The device is powered off or disconnected.",
        status: 'KO'
      })
    } else {
      
      // Connection strength
      glances.push({
        title: "Connection",
        status: latest.rssi > -70 ? "OK" : "WARN",
        text: latest.rssi > -70 ? "" : "The Wi-Fi signal to the device is poor."
      });

      glances.push({
        title: "Temperature",
        status: latest.waterTemp > 2 ? "OK" : "WARN",
        test: latest.waterTemp > 2 ? "" : "The water temperature is very low."
      })

    }
    return glances;
  }
}

module.exports = Device;