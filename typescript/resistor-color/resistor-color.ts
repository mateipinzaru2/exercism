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

export const colorCode = (color: string): number => {
  const normalizedColor = color.toLowerCase()
  const index = COLORS.findIndex((c) => c === normalizedColor)

  if (index === -1) {
    throw new Error(`Color "${color}" is not a valid resistor color.`)
  }

  return index
}
