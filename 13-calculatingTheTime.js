function calculateTime(deliveries) {
  const maxSeconds = 7 * 3600;
  const times = deliveries
    .map(function (deliver) {
      return deliver.split(":").map(Number);
    })
    .reduce((acc, time) => {
      return acc + time[0] * 3600 + time[1] * 60 + time[2];
    }, 0);

  const convertToTime = (seconds) => {
    const hours = `${Math.floor(seconds / 3600)}`.padStart(2, 0);
    const minutes = `${Math.floor((seconds % 3600) / 60)}`.padStart(2, 0);
    const remainingSeconds = `${seconds % 60}`.padStart(2, 0);
    return `${hours}:${minutes}:${remainingSeconds}`;
  };

  const difference = maxSeconds - times;
  const finalTime = convertToTime(Math.abs(difference));
  return difference <= 0 ? finalTime : `-${finalTime}`;
}

const time = calculateTime(["00:10:00", "01:00:00", "03:30:00"]);
// '-02:20:00'
console.log(time);

const time1 = calculateTime(["02:00:00", "05:00:00", "00:30:00"]);
// '00:30:00'
console.log(time1);

const time2 = calculateTime(["00:45:00", "00:45:00", "00:00:30", "00:00:30"]);
// '-05:29:00'
console.log(time2);

const time3 = calculateTime(["02:00:00", "03:00:00", "02:00:00"]);
// '00:00:00'
console.log(time3);
