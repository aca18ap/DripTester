const { PrismaClient } = require("@prisma/client");
const prisma = new PrismaClient();

const express = require("express");
const router = express.Router();

router.all("/:id/", async function(req, res) {
  if (!(req.params.id && req.params.id.length > 2)) return;
  console.log(req.body)
  const device = await prisma.device.findOne({
    where: { id: req.params.id }
  });

  if (device) {
    await prisma.dataEntry.create({
      data: {
        timestamp: new Date(),
        device: {
          connect: { id: req.params.id }
        },

        waterTemp: req.body.waterTemp,
        airTemp: req.body.airTemp,
        humidity: req.body.humidity,
        light: req.body.light,
        ph: req.body.ph,
        rssi: req.body.rssi,
        beds: req.body.beds ? { create: req.body.beds } : undefined
      }
    })
  } else {
    // unregistered device
    await prisma.unregisteredDevice.upsert({
      where: { id: req.params.id },
      create: {
        id: req.params.id,
        online: new Date()
      },
      update: {
        id: req.params.id,
        online: new Date()
      }
    })
  }

  res.send("OK");
});


module.exports = router;

