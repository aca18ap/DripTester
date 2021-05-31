const { PrismaClient } = require("@prisma/client");
const prisma = new PrismaClient();

const User = {
  location: (user) => {
    if (!user.latitude || !user.longitude) return null;
    return {
      latitude: user.latitude,
      longitude: user.longitude
    }
  },
  devices: async (user) => {
    return await prisma.device.findMany({
      where: {
        owner: user
      }
    })
  },
  groups: async (user) => {
    return await prisma.group.findMany({
      where: {
        members: {
          some: {
            id: user.id
          }
        }
      }
    })
  }
}

module.exports = User;