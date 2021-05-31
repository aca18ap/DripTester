const { PrismaClient } = require("@prisma/client");
const prisma = new PrismaClient();

const Group = {
  members: async (group) => {
    return await prisma.group.findOne({ where: { id: group.id } }).members();
  },
  devices: async (group) => {
    return await prisma.group.findOne({ where: { id: group.id } }).devices();
  }
}

module.exports = Group;