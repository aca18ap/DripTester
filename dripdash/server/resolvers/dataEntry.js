const { PrismaClient } = require("@prisma/client");
const prisma = new PrismaClient();

const DataEntry = {
  beds: async (dataEntry) => {
    return await prisma.bed.findMany({
      where: { dataEntryId: dataEntry.id }
    })
  }
};

module.exports = DataEntry;