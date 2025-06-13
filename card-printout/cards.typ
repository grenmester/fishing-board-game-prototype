#set page(margin: (rest: 0.25in))

#let data = yaml("card-data.yml")

#let genFish(fish) = {
  let topRow = grid(
    columns: (1fr, 1fr, 1fr),
    align(left, "$" + str(fish.money)),
    text(weight: "bold")[Fish],
    align(right, "R: " + str(fish.reputation)),
  )
  let subtitle = "(" + fish.habitat + ") - " + str(fish.size) + "cm, " + fish.color
  [
    #box(stroke: 1pt, height: 2.65in, width: 1.9in, inset: 0.1in)[
      #align(top + center, topRow)
      #align(top + center, "[" + fish.rarity + "]")
      #align(top + center, subtitle)
      *#align(top + center, box(height: 2em)[#text(size: 20pt, fish.name)])*
      #align(bottom + center, box(height: 2em)[#fish.requirement])
    ]
  ]
}

#let genGear(gear) = {
  let topRow = grid(
    columns: (1fr, 1fr, 1fr),
    align(left, "$" + str(gear.cost)),
    text(weight: "bold")[Gear],
    align(right, gear.category),
  )
  [
    #box(stroke: 1pt, height: 2.65in, width: 1.9in, inset: 0.1in)[
      #align(top + center, topRow)
      *#align(top + center, box(height: 2em)[#text(size: 20pt, gear.name)])*
      #align(bottom + center, box(height: 2em)[#gear.description])
    ]
  ]
}

#let genSkill(skill) = {
  let topRow = grid(
    columns: (1fr, 1fr, 1fr),
    align(left, "$2"),
    text(weight: "bold")[Skill],
    align(right, skill.category),
  )
  [
    #box(stroke: 1pt, height: 2.65in, width: 1.9in, inset: 0.1in)[
      #align(top + center, topRow)
      *#align(top + center, box(height: 2em)[#text(size: 20pt, skill.name)])*
      #align(bottom + center, box(height: 2em)[#skill.description])
    ]
  ]
}

#let genEvent(event) = {
  [
    #box(stroke: 1pt, height: 2.65in, width: 1.9in, inset: 0.1in)[
      #align(top + center, text(weight: "bold")[Event] + " (" + event.category + ")")
      *#align(top + center, box(height: 2em)[#text(size: 20pt, event.name)])*
      #align(bottom + center, box(height: 2em)[#event.description])
    ]
  ]
}

#let genQuest(quest) = {
  let topRow = grid(
    columns: (1fr, 1fr, 1fr),
    align(left, "$" + str(quest.money)),
    text(weight: "bold")[Quest],
    align(right, "R: " + str(quest.reputation)),
  )
  [
    #box(stroke: 1pt, height: 2.65in, width: 1.9in, inset: 0.1in)[
      #align(top + center, topRow)
      *#align(top + center, box(height: 2em)[#text(size: 20pt, quest.name)])*
      #align(bottom + center, box(height: 2em)[#quest.description])
    ]
  ]
}

#let genCards(data) = {
  for (category, v) in data {
    if (category == "fish") {
      for card in v {
        genFish(card)
      }
    }
    if (category == "gear") {
      for card in v {
        genGear(card)
      }
    }
    if (category == "skill") {
      for card in v {
        genSkill(card)
      }
    }
    if (category == "event") {
      for card in v {
        genEvent(card)
      }
    }
    if (category == "quest") {
      for card in v {
        genQuest(card)
      }
    }
  }
}

#genCards(data)
