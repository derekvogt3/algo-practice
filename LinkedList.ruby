class Node

    attr_accessor :data, :next

    def initialize(data,next_node = nil)
        @data = data
        @next = next_node
        
    end


end

class LinkedList

    def is_empty?

        if @head == nil
            return true

        else 
            return false

        end

    end


    def push(data)
        if self.is_empty?
            @head = Node.new(data)

        else

            current_node = @head
            new_node = Node.new(data)
            while current_node.next != nil
                current_node = current_node.next
            end

            current_node.next = new_node

        end
    end

    #unshift: add a new node in the front


    def unshift(data)
        if self.is_empty?

            @head = Node.new(data)

        else

            current_head = Node.new(data)
            current_head.next = @head
            @head = current_head

        end
        
    end
#pop: remove the last node and return it
    def pop

        if self.is_empty?
            return "empty linked list"
        else 
            current_node = @head

            while current_node.next.next != nil
                current_node = current_node.next

            end
            last_node = current_node.next
            current_node.next = nil
            return last_node
        end


    end


        #shift: remove the first node and return it

        def shift

            if self.is_empty?

                "linked list is empty"

            else

                return_value = @head
                new_head = @head.next
                @head.next = nil
                @head = new_head

                return return_value

            end
            
        end

    def size

        if self.is_empty?

            count = 0

        else

            count = 1
            
            current_node = @head
            while current_node.next != nil
                count += 1
                current_node = current_node.next

        end

        return count
    end 



end

def recursion_two_lists(list1,list2)

    if list1 == nil
        return list2

    elsif list2 == nil
        return list1

    elsif list1.val < list2.val

        list1.next = self.merge_two_lists(list1.next,list2)

        return list1

    else

        list2.next = self.merge_two_lists(list1,list2.next)

        return list2


end