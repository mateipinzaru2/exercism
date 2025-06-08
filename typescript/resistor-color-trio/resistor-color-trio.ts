/**
 * Resistor Color Trio - Clean TypeScript Implementation
 * Inspired by clean Python patterns for better readability
 */

const COLOR_CODES = {
  black: 0,
  brown: 1,
  red: 2,
  orange: 3,
  yellow: 4,
  green: 5,
  blue: 6,
  violet: 7,
  grey: 8,
  white: 9,
} as const

const MAGNITUDES = {
  tera: 12,
  giga: 9,
  mega: 6,
  kilo: 3,
} as const

export type Color = keyof typeof COLOR_CODES

/**
 * Returns resistor label given a list of known resistor band colors
 * @param colors Array of color names (minimum 3 required, extras ignored)
 * @returns Formatted resistance string with appropriate units
 */
export const decodedResistorValue = (colors: readonly string[]): string => {
  // Validation
  if (colors.length < 3) {
    throw new Error("At least three colors are required")
  }

  if (!colors.slice(0, 3).every((color) => color in COLOR_CODES)) {
    throw new Error(
      `Invalid resistor color in: ${colors.slice(0, 3).join(", ")}`
    )
  }

  // Extract color values and calculate resistance
  const [first, second, third] = colors.map(
    (color) => COLOR_CODES[color as Color]
  )
  const ohms = (first * 10 + second) * 10 ** third

  // Find appropriate magnitude and return formatted result
  const magnitude = Object.entries(MAGNITUDES)
    .sort(([, a], [, b]) => b - a)
    .find(([, magnitudeValue]) => ohms >= 10 ** magnitudeValue)

  return magnitude
    ? `${ohms / 10 ** magnitude[1]} ${magnitude[0]}ohms`
    : `${ohms} ohms`
}
