/**
 * Array of resistor color names in order of their numeric values (0-9)
 */
export const COLORS = [
  "black",
  "brown",
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "violet",
  "grey",
  "white",
]

/**
 * Gets the numeric value for a resistor color
 * @param color - The color name
 * @returns The numeric value (0-9) for the color
 */
const colorCode = (color: string): number => {
  const index = COLORS.indexOf(color.toLowerCase())
  if (index === -1) {
    throw new Error(`Invalid color: ${color}`)
  }
  return index
}

/**
 * Decodes the resistance value from the first two color bands
 * @param colors - Array of color names (only first two are used)
 * @returns Two-digit number representing the resistance value
 */
export function decodedValue(colors: string[]): number {
  if (colors.length < 2) {
    throw new Error("At least two colors are required")
  }

  const firstDigit = colorCode(colors[0])
  const secondDigit = colorCode(colors[1])

  return firstDigit * 10 + secondDigit
}
