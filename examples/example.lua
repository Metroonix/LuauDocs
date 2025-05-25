--- @class Player
--- @field name string
--- @field score number

local Player = {}
Player.__index = Player

--- @param name string
function Player.new(name)
    local self = setmetatable({}, Player)
    self.name = name
    self.score = 0
    return self
end

return Player