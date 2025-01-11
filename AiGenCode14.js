// Function to calculate the number of days between two dates
function getDaysBetweenDates(startDate, endDate) {
    const date1 = new Date(startDate);
    const date2 = new Date(endDate);

    return Math.round(Math.abs((date2.getTime() - date1.getTime()) / (1000 * 3600 * 24)));
}

// Function to generate a weekly schedule
function generateWeeklySchedule(year, month, day) {
    // Get the first day of the week (Monday = 1, Sunday = 0)
    const firstDayOfWeek = new Date(year, month - 1, day).getDay();
    let dayOfWeek = (firstDayOfWeek + 1) % 7;

    let schedule = [];
    for (let i = 0; i < 7; i++) {
        const date = new Date(year, month - 1, day);
        date.setDate(date.getDate() + i);

        // Add a comment for the current day
        schedule.push(`Monday ${i + 1}: Today is a great day!`);
        
        if (dayOfWeek === i) {
            schedule[i] = `Tuesday ${i + 1}: This is a Tuesday`;
        }

        dayOfWeek = (dayOfWeek + 1) % 7;
    }
    return schedule;
}

// Example usage
const year = 2024;
const month = 3;
const day = 20;

console.log(generateWeeklySchedule(year, month, day));
