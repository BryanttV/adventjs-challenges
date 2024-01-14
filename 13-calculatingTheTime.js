function calculateTime(deliveries) {
  const maxSeconds = 7 * 3600;
  const len = deliveries.length;
  const times = deliveries.map(function (deliver) {
    return deliver.split(":").map(Number);
  });

  let hours = 0;
  let minutes = 0;
  let seconds = 0;

  for (let i = 0; i < len; i++) {
    hours += times[i][0];
    minutes += times[i][1];
    seconds += times[i][2];
  }

  const convertToSeconds = (hours, minutes, seconds) => {
    let totalSeconds = seconds;
    totalSeconds += minutes * 60;
    totalSeconds += hours * 3600;
    return totalSeconds;
  };

  let totalSeconds = convertToSeconds(hours, minutes, seconds);

  const convertToTime = (seconds) => {
    const isNegative = seconds < 0 ? true : false;
    if (isNegative) {
      seconds *= -1;
    }
    const hours = Math.floor(seconds / 3600).toString();
    const minutes = Math.floor((seconds % 3600) / 60).toString();
    const remainingSeconds = (seconds % 60).toString();
    return `${isNegative ? "" : "-"}${hours.padStart(
      2,
      "0"
    )}:${minutes.padStart(2, "0")}:${remainingSeconds.padStart(2, "0")}`;
  };

  const difference = maxSeconds - totalSeconds;

  return difference == 0 ? "00:00:00" : convertToTime(difference);
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
