function Table(e)

  for _, body in ipairs(e.bodies) do
    for j = #body.body, 1, -1 do
      local row = body.body[j].cells
      local col_span = 1
      for i = #row, 1, -1 do
        local cell = row[i]
        -- print(cell, '<br>')

        -- if cell.contents[1] and cell.contents[1].content and cell.contents[1].content[1].text == '<' then
        --   table.remove(body.body[j].cells, i)
        -- end

        if cell.contents[1] and cell.contents[1].content and cell.contents[1].content[1].text == '>' then
          table.remove(body.body[j].cells, i)
          col_span = col_span + 1
        elseif col_span > 1 then
          -- cell.attr = {class = "pink"}
          cell.col_span = col_span
          col_span = 1
        end
      end
    end
  end

  for _, body in ipairs(e.bodies) do
    for j = #body.body[1].cells, 1, -1 do
      local row_span = 1
      for i = #body.body, 1, -1 do
        local cell = body.body[i].cells[j]
        if cell then
          if cell.contents[1] and cell.contents[1].content and cell.contents[1].content[1].text == '^' then
            table.remove(body.body[i].cells, j)
            row_span = row_span + 1
          elseif row_span > 1 then
            -- cell.attr = {class = "pink"}
            cell.row_span = row_span
            row_span = 1
          end
        end
      end
    end
  end

  for _, body in ipairs(e.bodies) do
    for j = #body.body, 1, -1 do
      local row = body.body[j].cells
      local col_span = 1
      for i = #row, 1, -1 do
        local cell = row[i]
        if cell.contents[1] and cell.contents[1].content and cell.contents[1].content[1].text then
          local class = cell.contents[1].content[1].text:match("{(%a+)}")
          if class then
            table.remove(cell.contents[1].content, 1)
            table.insert(cell.classes, class)
          end
        end
      end
    end
  end

  return e
end
